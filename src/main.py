from src.transactions_info import get_transactions_from_csv, get_transactions_from_xlsx
from src.utils import operations_data
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency
from src.find_operations_dicts import find_operations_by_description, operations_count
from src.widget import get_date, mask_account_card
from config import DATA_DIR
import os
from datetime import datetime

operations_path = os.path.join(DATA_DIR, "operations.json")
transactions_path = os.path.join(DATA_DIR, "transactions.csv")
transactions_path_excel = os.path.join(DATA_DIR, "transactions_excel.xlsx")

pathes = [operations_path, transactions_path, transactions_path_excel]
def main():
    global result_file
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
          "Выберите необходимый пункт меню:\n"
          "1. Получить информацию о транзакциях из JSON-файла\n"
          "2. Получить информацию о транзакциях из CSV-файла\n"
          "3. Получить информацию о транзакциях из XLSX-файла")
    num_transaction = input()
    while num_transaction not in ("1", "2", "3"):
        num_transaction = input("Выберите 1, 2 или 3\n")

    if num_transaction == "1":
        print("Для обработки выбран JSON-файл.")
        result_file = operations_data(operations_path)
        print(result_file)

    elif num_transaction == "2":
        print("Для обработки выбран CSV-файл.")
        result_file = get_transactions_from_csv(transactions_path)
        print(result_file)
    elif num_transaction == "3":
        print("Для обработки выбран XLSX-файл.")
        result_file = get_transactions_from_xlsx(transactions_path_excel)
        print(result_file)


    user_status = input("Введите статус, по которому необходимо выполнить фильтрацию.\n"
          "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n").lower()
    while user_status not in ("executed", "canceled", "pending"):
        user_status = input(f"Статус операции {user_status} недоступен\n")

    if user_status == "executed":
        result_file = filter_by_state(result_file, user_status.upper())
        print('Операции отфильтрованы по статусу "EXECUTED"')
        print(result_file)
    elif user_status == "canceled":
        result_file = filter_by_state(result_file, user_status.upper())
        print('Операции отфильтрованы по статусу "CANCELED"')
        print(result_file)
    elif user_status == "pending":
        filtered_file = filter_by_state(result_file, user_status.upper())
        print('Операции отфильтрованы по статусу "PENDING"')
        print(result_file)

    date_sort = input("Отсортировать операции по дате? Да/Нет\n").lower()
    while date_sort not in ("да", "нет"):
        date_sort = input("Введите да либо нет\n")
    if date_sort == "да":
        sort_up_down = input("Отсортировать по возрастанию или убыванию?\n").lower()
        while sort_up_down not in ("по возрастанию", "по убыванию"):
            sort_up_down = input("Введите 'по возрастанию' либо 'по убыванию'\n")
        if sort_up_down == "по возрастанию":
            result_file = sort_by_date(result_file, False)
        elif sort_up_down == "по убыванию":
            result_file = sort_by_date(result_file)
    current_sort = input("Выводить только рублевые транзакции? Да/Нет\n").lower()
    while current_sort not in ("да", "нет"):
        current_sort = input("Введите да либо нет\n")
    if current_sort == "да":
        result_file = list(filter_by_currency(result_file, "RUB"))

    description_sort = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").lower()
    while description_sort not in ("да", "нет"):
        description_sort = input("Введите да либо нет\n")
    if description_sort == "да":
        result_file = find_operations_by_description(result_file, "Открытие вклада")

    # return result_file


    print("Распечатываю итоговый список транзакций...\n")
    print(f"Всего банковских операций в выборке: {len(result_file)}")
    some_key = "from"
    for transaction in result_file:
        print(f"{get_date(transaction["date"])} {transaction["description"]}")

        if some_key in transaction.keys():
            print(f"{mask_account_card(transaction['to'])} -> {mask_account_card(transaction['from'])}")
        else:
            print(f"{mask_account_card(transaction['to'])}")
        print(f"Сумма: {transaction['operationAmount']["amount"]}")


    # return result_file


# def result_output(result_file):
#     print("Распечатываю итоговый список транзакций...\n")
#     # print(f"Всего банковских операций в выборке: {len(result_file)}")
#     for transaction in result_file:
#         print()




if __name__ == '__main__':
    # print(filter_by_status(source_file))
    main()
    # print(len(main(result_file)))

    # for i in main():
    #     print(i)




