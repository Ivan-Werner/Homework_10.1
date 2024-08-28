import os
import requests
from dotenv import load_dotenv
load_dotenv()

test_transaction_rub = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }

test_transaction_usd = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }


def convert_to_rub(transaction: dict) -> float:
    """Функция выдает сумму транзакции в рублях и конвертирует в рубли из других валют"""
    code = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]
    if code == "RUB":
        return amount
    else:
        url = f"https://api.apilayer.com/fixer/convert?to=RUB&from={code}&amount={amount}"
        token = os.getenv("API_KEY")
        headers = {"apikey": token}
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise RuntimeError
        return response.json()["result"]


if __name__ == "__main__":
    print(convert_to_rub(test_transaction_usd))
