import requests


def get_currency_rate(currency_code):
    url = f"https://www.cbr-xml-daily.ru//daily_json.js"
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Failed to get currency rate")
    data = response.json()
    currency_data = data["Valute"].get(currency_code)
    if not currency_data:
        raise ValueError(f"No data for currency {currency_code}")
    return {
        "currency_code": currency_code,
        "rate": currency_data["Value"],
    }

print(get_currency_rate("BYN"))
