import json
import logging
from datetime import datetime

import requests

from config import PATH

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(PATH / "logs" / "views.log", "w", encoding="UTF-8")
file_formatter = logging.Formatter(
    "[%(asctime)s.%(msecs)03d] [%(levelname)-7s] - %(name)r - (%(filename)s).%(funcName)s:%(lineno)-3d - %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def load_user_settings():
    try:
        logger.info("Загрузка пользовательских настроек")
        with open(PATH / "user_settings.json", "r", encoding="UTF-8") as f:
            return json.load(f)
    except Exception as ex:
        logger.error("Ошибка загрузки 'user_settings.json': %s", ex)
        return []


def get_greeting(date_time):
    logger.info("Запуск функции %s со значением %s", get_greeting.__name__, date_time)
    try:
        time_obj = datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")
    except ValueError as ex:
        logger.error("Ошибка обработки даты: %s", ex)
        time_obj = datetime.now()

    if 5 <= time_obj.hour < 12:
        return "Доброе утро!"
    elif 12 <= time_obj.hour < 17:
        return "Добрый день!"
    elif 17 <= time_obj.hour < 24:
        return "Добрый вечер!"
    else:
        return "Доброй ночи!"


def get_date(date_time):
    try:
        date_obj = datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")
        start_month_obj = date_obj.replace(day=1, hour=0, minute=0, second=0)
        return start_month_obj.strftime("%Y-%m-%d"), date_obj.strftime("%Y-%m-%d")
    except ValueError as ex:
        now = datetime.now()
        start_month_obj = now.replace(day=1, hour=0, minute=0, second=0)
        return start_month_obj.strftime("%Y-%m-%d"), now.strftime("%Y-%m-%d")


def get_currency(user_currencies):
    result = {}
    try:
        url = f"https://www.cbr-xml-daily.ru/daily_json.js"
        response = requests.get(url)
        status_code = response.status_code
        if status_code == 200:
            for currency in user_currencies:
                if currency in response.json()["Valute"]:
                    result[currency] = response.json()["Valute"][currency]["Value"]
                else:
                    result[currency] = "Нет данных"
        else:
            return f"Не успешный запрос.\nКод ошибки: {status_code}."
    except Exception as ex:
        logger.error("Ошибка получения курсов %s", ex)
    return result


# def get_stock_prices(stocks):
#     prices = {}
#     for stock in stocks:
#         logging.debug(f"Запрос цены для акции: {stock}")
#         try:
#             response = requests.get(
#                 f"https://api.marketstack.com/v1/eod?access_key=df3caee3a4eb8c55e2af01775ca399c8&symbols=AAPL {stock}"
#             )
#             response.raise_for_status()  # Проверка на ошибки HTTP
#             prices[stock] = response.json().get("price", None)
#             logging.info(f"Успешно получена цена для {stock}: {prices[stock]}")
#         except requests.RequestException as e:
#             logging.error(f"Ошибка при получении цены для {stock}: {e}")
#             prices[stock] = None
#     return prices
