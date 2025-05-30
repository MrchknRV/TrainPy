import json
import logging
from datetime import datetime
import requests


# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def load_user_settings():
    """Загрузка пользовательских настроек из файла user_settings.json"""
    try:
        with open("user_settings.json", "r") as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Ошибка загрузки user_settings.json: {e}")
        return {"user_currencies": ["USD", "EUR"], "user_stocks": ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]}


def get_greeting(time_str):
    """Возвращает приветствие в зависимости от времени"""
    try:
        time_obj = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S").time()
    except ValueError:
        time_obj = datetime.now().time()

    if 5 <= time_obj.hour < 12:
        return "Доброе утро"
    elif 12 <= time_obj.hour < 17:
        return "Добрый день"
    elif 17 <= time_obj.hour < 23:
        return "Добрый вечер"
    else:
        return "Доброй ночи"


def get_month_start_end(date_str):
    """Возвращает даты начала месяца и входящую дату"""
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        month_start = date_obj.replace(day=1, hour=0, minute=0, second=0)
        return month_start.strftime("%Y-%m-%d"), date_obj.strftime("%Y-%m-%d")
    except ValueError:
        logger.error("Неверный формат даты, используется текущая дата")
        now = datetime.now()
        month_start = now.replace(day=1, hour=0, minute=0, second=0)
        return month_start.strftime("%Y-%m-%d"), now.strftime("%Y-%m-%d")


def get_currency_rates(currencies):
    """Получение курсов валют через API"""
    rates = {}
    try:
        # Используем API Центробанка России для курсов валют
        response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
        data = response.json()

        for currency in currencies:
            if currency in data["Valute"]:
                rates[currency] = data["Valute"][currency]["Value"]
            else:
                rates[currency] = "Нет данных"
    except Exception as e:
        logger.error(f"Ошибка получения курсов валют: {e}")
        for currency in currencies:
            rates[currency] = "Ошибка"

    return rates


def get_stock_prices(stocks):
    """Получение цен акций через API"""
    prices = {}
    try:
        # Используем Alpha Vantage API для получения цен акций
        for stock in stocks:
            try:
                api_key = "YOUR_ALPHAVANTAGE_API_KEY"  # Замените на реальный API ключ
                url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock}&apikey={api_key}"
                response = requests.get(url)
                data = response.json()
                prices[stock] = float(data["Global Quote"]["05. price"])
            except:
                prices[stock] = "Нет данных"
    except Exception as e:
        logger.error(f"Ошибка получения цен акций: {e}")
        for stock in stocks:
            prices[stock] = "Ошибка"

    return prices


def generate_main_page_data(date_str, cards_data):
    """Генерация данных для главной страницы"""
    settings = load_user_settings()

    # 1. Приветствие
    greeting = get_greeting(date_str)

    # 2. Данные по картам
    cards_info = []
    for card in cards_data:
        card_info = {
            "last_four": card["number"][-4:],
            "total_spent": card["total_spent"],
            "cashback": card["total_spent"] // 100,
        }
        cards_info.append(card_info)

    # 3. Топ-5 транзакций
    all_transactions = []
    for card in cards_data:
        all_transactions.extend(card["transactions"])

    top_transactions = sorted(all_transactions, key=lambda x: x["amount"], reverse=True)[:5]

    # 4. Курсы валют
    currencies = settings.get("user_currencies", ["USD", "EUR"])
    currency_rates = get_currency_rates(currencies)

    # 5. Цены акций
    stocks = settings.get("user_stocks", ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"])
    stock_prices = get_stock_prices(stocks)

    return {
        "greeting": greeting,
        "cards": cards_info,
        "top_transactions": top_transactions,
        "currency_rates": currency_rates,
        "stock_prices": stock_prices,
    }


def main(date_time_str):
    """Главная функция для обработки запроса"""
    # В реальном приложении здесь бы получали данные карт из БД
    # Для примера используем тестовые данные
    test_cards_data = [
        {
            "number": "427601******1234",
            "total_spent": 12500,
            "transactions": [
                {"id": 1, "amount": 5000, "date": "2020-05-15", "description": "Магазин"},
                {"id": 2, "amount": 3000, "date": "2020-05-10", "description": "Ресторан"},
                {"id": 3, "amount": 4500, "date": "2020-05-05", "description": "Путешествие"},
            ],
        },
        {
            "number": "546901******5678",
            "total_spent": 8700,
            "transactions": [
                {"id": 4, "amount": 2000, "date": "2020-05-12", "description": "Супермаркет"},
                {"id": 5, "amount": 500, "date": "2020-05-08", "description": "Кино"},
                {"id": 6, "amount": 6200, "date": "2020-05-03", "description": "Отель"},
            ],
        },
    ]

    data = generate_main_page_data(date_time_str, test_cards_data)
    return json.dumps(data, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    # Пример вызова с текущей датой и временем
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(main(current_datetime))
