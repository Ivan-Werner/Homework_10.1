import os
from unittest.mock import patch

import pytest

from src.external_api import convert_to_rub


def _create_transaction(currency_code: str, amount: float) -> dict:
    return {
        'operationAmount': {'currency': {'code': currency_code}, 'amount': amount},
    }

@patch('requests.get')
def test_rubles_amount(mock_get):
    transaction = _create_transaction('RUB', 30.0)

    result = convert_to_rub(transaction)

    assert result == 30.0
    mock_get.assert_not_called()


@patch('requests.get')
def test_usd_amount_invalid_status_code(mock_get):
    transaction = _create_transaction('USD', 30.0)
    mock_get.return_value.status_code = 400

    with pytest.raises(RuntimeError):
        convert_to_rub(transaction)


@patch('requests.get')
def test_usd_amount_valid_status_code(mock_get):
    transaction = _create_transaction('USD', 30.0)
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'result': 10.0}

    result = convert_to_rub(transaction)

    assert result == 10.0
