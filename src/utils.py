import logging
import os
import json
from config import DATA_DIR, LOG_DIR

operations_path = os.path.join(DATA_DIR, "operations.json")
utils_log_path = os.path.join(LOG_DIR, "utils.log")

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
# file_handler = logging.FileHandler("..\\logs\\utils.log", mode='w+')
file_handler = logging.FileHandler(utils_log_path, mode='w+')
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s : %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def operations_data(operations_path: str) -> list:
    """Функция возвращает список словарей с данными о финансовых транзакциях из JSON-файла"""
    try:
        logger.info("Открывается JSON-файл")
        with open(operations_path, encoding='utf-8') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        logger.error("Ошибка: файл не найден или файл пустой")
        data = []


    if data == [] or type(data) != list:
        logger.error("JSON - файл является пустым списком или не является списком")
        return []
    else:
        logger.info("Вывод данных о транзакциях")
        return data


if __name__ == "__main__":
    print(operations_data(operations_path))
