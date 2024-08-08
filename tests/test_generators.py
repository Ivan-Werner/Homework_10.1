from src.generators import (filter_by_currency, transaction_descriptions,
                            card_number_generator)

def test_filter_by_currency(correct_filter_by_currency):
    assert filter_by_currency([{
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
        }], "USD") == correct_filter_by_currency




# @pytest.mark.parametrize("info, expected", [{
#             "id": 939719570,
#             "state": "EXECUTED",
#             "date": "2018-06-30T02:08:58.425572",
#             "operationAmount": {
#                 "amount": "9824.07",
#                 "currency": {
#                     "name": "USD",
#                     "code": "USD"
#                 }
#             }, "Перевод организации"
#     ])
# def test_transaction_descriptions(info, expected):
#     assert transaction_descriptions(info) == expected


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





