import pytest


@pytest.fixture
def num_card():
    return '7000 79** **** 6361'


@pytest.fixture
def num_card_empty():
    return 'Неверный формат номера карты'


@pytest.fixture
def num_card_less():
    return 'Неверный формат номера карты'


@pytest.fixture
def num_bill():
    return '**4305'


@pytest.fixture
def num_bill_empty():
    return 'Неверный формат номера счета'


@pytest.fixture
def num_bill_wrong():
    return 'Неверный формат номера счета'


@pytest.fixture
def correct_date():
    return ('11.03.2024')


@pytest.fixture
def empty_date():
    return ('')


@pytest.fixture
def state_executed():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


@pytest.fixture
def same_date():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.425572'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.419441'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.241689'}]
