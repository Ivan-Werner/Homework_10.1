import pytest

from src.generators import (filter_by_currency, transaction_descriptions,
                            card_number_generator)


def test_filter_by_currency(transactions_fix):
    iterator = filter_by_currency(transactions_fix, "USD")
    assert next(iterator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    }

    assert next(iterator) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    }

    assert next(iterator) == {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {
            "amount": "56883.54",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229"
    }


@pytest.mark.parametrize(
    "transactions, currency, expected", [([], "", "Введен пустой список."), ([], "RUB", "Введен пустой список.")]
)
def test_filter_by_currency_exceptions(transactions, currency, expected):
    res = filter_by_currency(transactions, currency)
    assert res == expected


def test_transaction_descriptions(transactions_fix):
    iterator = transaction_descriptions(transactions_fix)
    assert next(iterator) == "Перевод организации"
    assert next(iterator) == "Перевод со счета на счет"


def test_card_number_generator():
    generator = card_number_generator(1, 3)
    assert next(generator) == '0000 0000 0000 0001'
    assert next(generator) == '0000 0000 0000 0002'


def test_card_number_generator_low():
    generator = card_number_generator(0, 1)
    assert next(generator) == '0000 0000 0000 0000'
    assert next(generator) == '0000 0000 0000 0001'


def test_card_number_generator_high():
    generator = card_number_generator(9999999999999998, 9999999999999999)
    assert next(generator) == '9999 9999 9999 9998'
    assert next(generator) == '9999 9999 9999 9999'
