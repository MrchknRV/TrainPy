import os
import re

from src.generators import filter_by_currency
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.transactions_csv_excel import transactions_csv, transactions_excel
from src.utils import financial_transactions


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    menu = int(input("""Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла
    : """))
    if menu == 1:
        print("Для обработки выбран JSON-файл.")
        path_to_file = os.path.join(os.path.dirname(__file__), "data", "operations.json")
        trans = financial_transactions(path_to_file)

    elif menu == 2:
        print("Для обработки выбран CSV-файл.")
        path = os.path.join(os.path.dirname(__file__), "data", "transactions.csv")
        trans = transactions_csv(path)

    else:
        print("Для обработки выбран XLSX-файл.")
        path = os.path.join(os.path.dirname(__file__), "data", "transactions_excel.xlsx")
        trans = transactions_excel(path)

    state = input("""Введите статус, по которому необходимо выполнить фильтрацию. 
            Доступные для фильтровки статусы: 
            EXECUTED, CANCELED, PENDING
            :""")
    state = state.upper()
    while state != 'EXECUTED' and state != 'CANCELED' and state != 'PENDING':
        print(f'Статус операции "{state}" недоступен.')
        state = input("""Введите статус, по которому необходимо выполнить фильтрацию. 
                    Доступные для фильтровки статусы: 
                    EXECUTED, CANCELED, PENDING
                    :""")
        state = state.upper()
    else:
        if state == "EXECUTED":
            print('Операции отфильтрованы по статусу "EXECUTED"')
        elif state == 'CANCELED':
            print('Операции отфильтрованы по статусу "CANCELED"')
        else:
            print('Операции отфильтрованы по статусу "PENDING"')

    filter_trans = filter_by_state(trans, state)

    data_filter = input("""Отсортировать операции по дате? Да/Нет
    :""")
    sort = input("""Отсортировать по возрастанию или по убыванию?
    :""")
    sort = sort.lower()
    if sort == 'по возрастанию':
        sort_key = False
    else:
        sort_key = True

    new_filter_trans = sort_by_date(filter_trans, sort_key)

    code = input("""Выводить только рублевые тразакции? Да / Нет
    :""")
    code = code.upper()
    if code == 'ДА':
        new_filter_trans = filter_by_currency(new_filter_trans, 'RUB')

    filter_word = input("""Отфильтровать список транзакций по определенному слову в описании? Да/Нет
    : """)

    print('Распечатываю итоговый список транзакций...')

    if len(new_filter_trans) == 0:
        print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')

    print(f'Всего банковских операций в выборке: {len(new_filter_trans)}')

    if menu == 1:
        for x in new_filter_trans:
            if x["description"] == "Открытие вклада":
                print(f'{x["date"]} {x["description"]}')
                pattern = r'\b\d+\b'
                numer = re.findall(pattern, x["to"])
                numer = ''.join(numer)
                print(f'Счет{get_mask_account(numer)}')
                print(f'Сумма: {x["operationAmount"]["amount"]} {x["operationAmount"]["currency"]["name"]}')
            else:
                print(f'{x["date"]} {x["description"]}')
                pattern = r'\b\d+\b'
                pattern1 = r'\b[A-Za-zА-Яа-яЁё]+\b'

                text = x["from"]
                numer_from = re.findall(pattern, text)
                numer_from = ''.join(numer_from)
                name_from = re.findall(pattern1, text)
                name_from = ''.join(name_from)

                text_to = x["to"]
                numer_to = re.findall(pattern, text_to)
                numer_to = ''.join(numer_to)
                name_to = re.findall(pattern1, text_to)
                name_to = ''.join(name_to)

                if name_from == 'Счет':
                    numer_from_mask = get_mask_account(numer_from)
                else:
                    numer_from_mask = get_mask_card_number(numer_from)
                if name_to == 'Счет':
                    numer_to_mask = get_mask_account(numer_to)
                else:
                    numer_to_mask = get_mask_card_number(numer_to)
                print(f'{name_from} {numer_from_mask} -> {name_to} {numer_to_mask}')
                print(f'Сумма: {x["operationAmount"]["amount"]} {x["operationAmount"]["currency"]["name"]}')
    else:
        for x in new_filter_trans:
            if x["description"] == "Открытие вклада":
                print(f'{x["date"]} {x["description"]}')
                pattern = r'\b\d+\b'
                numer = re.findall(pattern, x["to"])
                numer = ''.join(numer)
                print(f'Счет{get_mask_account(numer)}')
                print(f'Сумма: {x["amount"]} {x["currency_name"]}')
            else:
                print(f'{x["date"]} {x["description"]}')
                pattern = r'\b\d+\b'
                pattern1 = r'\b[A-Za-zА-Яа-яЁё]+\b'

                text = x["from"]
                numer_from = re.findall(pattern, text)
                numer_from = ''.join(numer_from)
                name_from = re.findall(pattern1, text)
                name_from = ''.join(name_from)

                text_to = x["to"]
                numer_to = re.findall(pattern, text_to)
                numer_to = ''.join(numer_to)
                name_to = re.findall(pattern1, text_to)
                name_to = ''.join(name_to)

                if name_from == 'Счет':
                    numer_from_mask = get_mask_account(numer_from)
                else:
                    numer_from_mask = get_mask_card_number(numer_from)
                if name_to == 'Счет':
                    numer_to_mask = get_mask_account(numer_to)
                else:
                    numer_to_mask = get_mask_card_number(numer_to)
                print(f'{name_from} {numer_from_mask} -> {name_to} {numer_to_mask}')
                print(f'Сумма: {x["amount"]} {x["currency_name"]}')


if __name__ == '__main__':
    main()