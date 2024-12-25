import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("info, expected", [
    ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
    ('Счет 64686473678894779589', 'Счет **9589'),
    ('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),
    ('Счет 35383033474447895560', 'Счет **5560'),
    ('Visa Classic 6831982476737658', 'Visa Classic 6831 98** **** 7658')
])

def test_mask_account_card(info, expected):
    assert mask_account_card(info) == expected


def test_get_date(correct_date):
    assert get_date('2024-03-11T02:26:18.671407') == correct_date


def test_get_date_empty(empty_date):
    assert get_date('') == empty_date
