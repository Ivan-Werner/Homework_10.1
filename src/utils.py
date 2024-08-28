import os
import json
from config import DATA_DIR

operations_path = os.path.join(DATA_DIR, "operations.json")


def operations_data(operations_path: str) -> list:
    """Функция возвращает список словарей с данными о финансовых транзакциях из JSON-файла"""
    try:
        with open(operations_path, encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []
    if data == [] or type(data) != list:
        return []
    else:
        return data


if __name__ == "__main__":
    print(operations_data(operations_path))
