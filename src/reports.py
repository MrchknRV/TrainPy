import logging
from datetime import datetime, timedelta
from functools import wraps
from typing import Optional
from config import PATH
import pandas as pd
from src.file_reader import reader_file_xlsx
import json


logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(PATH / "logs" / "logging.log", "w", encoding="UTF-8")
file_formatter = logging.Formatter(
    "[%(asctime)s.%(msecs)03d] [%(levelname)-7s] - %(name)r - (%(filename)s).%(funcName)s:%(lineno)-3d - %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def log_report_to_file(filename=None):
    """Декоратор для записи отчета в файл."""

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            df = func(*args, **kwargs)
            logger.info("Проверка файла")
            if filename:
                logger.info("Проверка, являются ли данные датафреймом")
                if isinstance(df, pd.DataFrame):
                    logger.info("Запись отчёта в файл")
                    with open(PATH / "logs" / filename, "w", encoding="UTF-8") as f:
                        # df.to_json(filename, orient="records", lines=True, force_ascii=False, indent=4)
                        json.dump(df.to_dict(), f, ensure_ascii=False, indent=4)
                else:
                    logger.error("Данные не являются датафреймом. В файл записаны не будут")
            else:
                logger.warning("Файл не задан! Файл будет создан на основе текущей даты")
                if isinstance(df, pd.DataFrame):
                    date = datetime.now().strftime("%d.%m.%Y")
                    logger.info("Запись отчёта в файл")
                    with open(PATH / "logs" / f"{date}-report_file.json", "w", encoding="UTF-8") as f:
                        # df.to_json(filename, orient="records", lines=True, force_ascii=False, indent=4)
                        json.dump(df.to_dict(), f, ensure_ascii=False, indent=4)
                else:
                    logger.error("Данные не являются датафреймом. В файл записаны не будут")
            return df

        return inner

    return wrapper


@log_report_to_file()
def spending_by_category(data: pd.DataFrame, category: str, date: Optional[str] = None) -> pd.DataFrame:
    """Функция возвращает траты по заданной категории за последние три месяца (от переданной даты)."""
    try:
        required_data = {"Дата операции", "Номер карты", "Сумма операции", "Категория", "Описание"}
        logger.debug("Проверка файла на содержание колонок: %s", required_data)
        if not required_data.issubset(data.columns):
            missing = required_data - set(data.columns)
            logger.error("В файле отсутствуют необходимые колонки: %s", missing)
            raise ValueError(f"В файле отсутствуют необходимые колонки: {missing}")

        if date is None:
            date = datetime.now()
        else:
            date = datetime.strptime(date, "%Y-%m-%d")

        three_months = date - timedelta(days=90)
        data["Дата операции"] = pd.to_datetime(data["Дата операции"], format="%d.%m.%Y %H:%M:%S")
        filtered_data = data[
            (data["Категория"] == category) & (data["Дата операции"] >= three_months) & (data["Дата операции"] <= date)
        ]

        if filtered_data.empty:
            logger.warning(f"Нет расходов для категории '{category}' за указанный период.")
            return pd.DataFrame(
                {
                    "category": [category],
                    "total_expenses": [0],
                    "date_from": [three_months.strftime("%Y-%m-%d")],
                    "date_to": [date.strftime("%Y-%m-%d")],
                }
            )

        total_spend = filtered_data["Сумма операции"].sum()
        report_file = pd.DataFrame(
            {
                "category": [category],
                "total_expenses": [float(round(total_spend, 2))],
                "date_from": [three_months.strftime("%Y-%m-%d")],
                "date_to": [date.strftime("%Y-%m-%d")],
            }
        )

        logger.info(f"Отчет создан для категории '{category}'")
        return report_file
    except FileNotFoundError:
        logger.error("Произошла ошибка: Файл не найден")
        return pd.DataFrame({"ERROR": ["Файл не найден"]})
    except Exception as ex:
        logger.error("Произошла ошибка: %s", ex)
        return pd.DataFrame({"ERROR": [f"Произошла ошибка: {str(ex)}"]})


print(spending_by_category(reader_file_xlsx("../data/operations.xlsx"), "Каршеринг", "2021-11-28"))
