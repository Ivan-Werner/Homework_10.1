import csv
import os
import pandas as pd
from config import DATA_DIR

from unittest.mock import patch

transactions_path = os.path.join(DATA_DIR, "transactions.csv")
transactions_path_excel = os.path.join(DATA_DIR, "transactions_excel.xlsx")



def get_transactions_from_csv(transactions_path: str) -> list:
    """Получаем данные о транзакциях в виде списка словарей из CSV-файла"""
    try:
        with open(transactions_path) as file:
            transactions_list = []
            py_file = csv.DictReader(file, delimiter=";")
            for row in py_file:
                transactions_list.append(row)
        return transactions_list
    except Exception:
        return []

def get_transactions_from_xlsx(transactions_path_excel: str) -> list:
    """Получаем данные о транзакциях в виде списка словарей из Excel-файла"""
    try:
        py_file = pd.read_excel(transactions_path_excel)
        py_dict = py_file.to_dict(orient='records')
        return py_dict
    except Exception:
        return []



if __name__ == '__main__':
    print(get_transactions_from_csv(transactions_path))
    # print(get_transactions_from_xlsx(transactions_path_excel))
