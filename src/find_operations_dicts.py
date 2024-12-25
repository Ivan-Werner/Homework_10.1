import re
import os
from collections import Counter
from config import DATA_DIR
from src.transactions_info import get_transactions_from_csv, get_transactions_from_xlsx

transactions_path = os.path.join(DATA_DIR, "transactions.csv")
transactions_path_excel = os.path.join(DATA_DIR, "transactions_excel.xlsx")

operations = get_transactions_from_csv(transactions_path)
def find_operations_by_description(operations: list, pattern: str) -> list:
    # user_str = input("Введите название банковской операции: ")
    res_list = []
    for i in operations:
        for k, v in i.items():
            if k == "description" and re.findall(pattern.lower(), v.lower()):
                res_list.append(i)

    return res_list


def operations_count(operations: list) -> dict:
    operations_list = []
    for operation in operations:
        for k, v in operation.items():
            if k == "description":
                operations_list.append(v)
    result = Counter(operations_list)
    return dict(result)

if __name__ == '__main__':
   # print(find_operations_by_description(get_transactions_from_csv(transactions_path)), "Перевод")
   # print(operations_count(get_transactions_from_csv(transactions_path)))
   # print(type(operations_count(get_transactions_from_csv(transactions_path))))
   print(find_operations_by_description(operations, "с карты на карту"))