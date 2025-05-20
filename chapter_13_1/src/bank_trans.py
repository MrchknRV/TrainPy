import re
from collections import Counter


def filter_banking_transactions_by_description(banking_description: list, search_bar: str) -> list:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска, а возвращает список словарей,
    у которых в описании есть данная строка."""
    pattern = search_bar
    string_ = []
    for description in banking_description:
        dict_string = str(description)
        if re.search(pattern, dict_string, flags=re.IGNORECASE):
            string_.append(dict_string)
    return string_


def filter_banking_description(banking_description: list, categories_operations: list) -> dict:
    """Функция принимает список словарей с данными о банковских операциях и список категорий операций, а возвращает
    словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории.
    Категории операций хранятся в поле description."""

    string = []
    for categories in categories_operations:
        pattern = categories
        description = str(banking_description)
        string_ = re.findall(pattern, description, flags=re.IGNORECASE)
        string = string + string_

    result = Counter(string)
    return result