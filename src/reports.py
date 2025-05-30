import logging
from datetime import datetime, timedelta
from functools import wraps
from typing import Optional

import pandas as pd
from src.file_reader import reader_file_xlsx


# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def log_report_to_file(filename):
    """Декоратор для записи отчета в файл."""

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            df = func(*args, **kwargs)
            logger.info("Проверка: являются ли данные датафреймом")
            if isinstance(df, pd.DataFrame):
                logger.info("Запись отчёта в файл")
                df.to_json(filename, orient="records", lines=True, force_ascii=False, indent=4)
            else:
                logger.error("Данные не являются датафреймом. В файл записаны не будут")
            return df

        return inner

    return wrapper


@log_report_to_file("spending.json")
def spending_by_category(data: pd.DataFrame, category: str, date: Optional[str] = None) -> pd.DataFrame:
    """Функция для вычисления трат по категории за последние три месяца."""

    if "Категория" not in data.columns:
        logger.error("Столбец 'Категория' не найден.")
        return pd.DataFrame()

    if date is None:
        date = datetime.now()
    else:
        date = datetime.strptime(date, "%Y-%m-%d")

    three_months_ago = date - timedelta(days=90)
    data["Дата операции"] = pd.to_datetime(data["Дата операции"], format="%d.%m.%Y %H:%M:%S")
    filtered_expenses = data[
        (data["Категория"] == category) & (data["Дата операции"] >= three_months_ago) & (data["Дата операции"] <= date)
    ]

    # Если нет расходов, возвращаем DataFrame с информацией об этом
    if filtered_expenses.empty:
        logger.warning(f"Нет расходов для категории '{category}' за указанный период.")
        return pd.DataFrame(
            {
                "category": [category],
                "total_expenses": [0],
                "date_from": [three_months_ago.strftime("%Y-%m-%d")],
                "date_to": [date.strftime("%Y-%m-%d")],
            }
        )

    # Создаем отчет в виде DataFrame
    total_expenses = filtered_expenses["Сумма операции"].sum()
    report_df = pd.DataFrame(
        {
            "category": [category],
            "total_expenses": [total_expenses],
            "date_from": [three_months_ago.strftime("%Y-%m-%d")],
            "date_to": [date.strftime("%Y-%m-%d")],
        }
    )

    logger.info(f"Отчет создан для категории '{category}'")
    return report_df


print(spending_by_category(reader_file_xlsx("../data/operations.xlsx"), "Каршеринг", "2021-11-28"))
