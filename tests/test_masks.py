from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(num_card):
    assert get_mask_card_number('7000792289606361') == num_card


def test_get_mask_card_number_empty(num_card_empty):
    assert get_mask_card_number('') == num_card_empty


def test_get_mask_card_number_less(num_card_less):
    assert get_mask_card_number('7365410843013') == num_card_less


def test_get_mask_account(num_bill):
    assert get_mask_account('73654108430135874305') == num_bill


def test_get_mask_account_empty(num_bill_empty):
    assert get_mask_account('') == num_bill_empty


def test_get_mask_account_wrong(num_bill_wrong):
    assert get_mask_account('736541084301A') == num_bill_wrong

