from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(bank_info: str) -> str:
    """Маскирует вводимые данные по номерам карта и счетов"""
    global result
    number = ''
    text = ''
    for i in bank_info:
        if i.isdigit():
            number += i
        else:
            text += i
    if len(number) == 16:
        result = get_mask_card_number(number)
    elif len(number) == 20:
        result = get_mask_account(number)
    return text + result


def get_date(date: str) -> str:
    """Преобразует вводимую дату к формату ДД.ММ.ГГГГ"""
    date_cut = date[:10].split('-')
    result = '.'.join(date_cut[::-1])
    return result


if __name__ == '__main__':
    print(mask_account_card('Счет 76145988629288763144'))

    print(get_date('2024-03-11T02:26:18.671407'))
