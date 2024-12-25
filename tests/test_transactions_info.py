import csv

import pandas as pd

from src.transactions_info import get_transactions_from_csv, get_transactions_from_xlsx
from unittest.mock import patch
from unittest.mock import mock_open
import pytest
import os
from config import DATA_DIR

transactions_path = os.path.join(DATA_DIR, "transactions.csv")
transactions_path_excel = os.path.join(DATA_DIR, "transactions_excel.xlsx")


def test_get_transaction_from_csv_wrong(wrong_transaction_csv):
    assert get_transactions_from_csv("wrong.csv") == wrong_transaction_csv


# @patch('pandas.read_csv')
# def test_def_transactions_from_csv(mock_read_csv):
#     mock_read_csv.return_value = []
#     assert get_transactions_from_csv(mock_read_csv) == []


def test_get_transaction_from_excel_wrong(wrong_transaction_excel):
    assert get_transactions_from_xlsx("wrong.xlsx") == wrong_transaction_excel



@patch('src.transactions_info.pd.read_excel')
def test_get_transactions_from_xlsx(mock_read, test_df):
    mock_read.return_value = test_df
    result = get_transactions_from_xlsx(transactions_path_excel)
    expected = test_df.to_dict(orient='records')
    assert result == expected






