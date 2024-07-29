def get_mask_card_number(card_num: str) -> str:
    """Возвращает маску номера карты по правилу по правилу XXXX XX** **** XXXX"""
    return card_num[:4] + " " + card_num[4:6] + "** **** " + card_num[-4:]


def get_mask_account(bill_num: str) -> str:
    """Возвращает маску номера по правилу **XXXX"""
    return "**" + bill_num[-4:]
