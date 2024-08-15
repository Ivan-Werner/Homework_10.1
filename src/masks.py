def get_mask_card_number(card_num: str) -> str:
    """Возвращает маску номера карты по правилу по правилу XXXX XX** **** XXXX"""
    if len(card_num) == 16 and card_num.isdigit():
        return card_num[:4] + " " + card_num[4:6] + "** **** " + card_num[-4:]
    else:
        return 'Неверный формат номера карты'


def get_mask_account(bill_num: str) -> str:
    """Возвращает маску номера по правилу **XXXX"""
    if len(bill_num) == 20 and bill_num.isdigit():
        return "**" + bill_num[-4:]
    else:
        return 'Неверный формат номера счета'


if __name__ == '__main__':
    print(get_mask_card_number('7000792289606361'))
    print(get_mask_account('73654108430135874305'))
