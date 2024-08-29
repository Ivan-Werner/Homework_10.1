import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("..\\logs\\masks.log", mode='w+')
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s : %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


logger.info("Запрос номера карты")


def get_mask_card_number(card_num: str) -> str:
    """Возвращает маску номера карты по правилу по правилу XXXX XX** **** XXXX"""

    if len(card_num) == 16 and card_num.isdigit():
        logger.info("Вывод маскированного номера карты")
        return card_num[:4] + " " + card_num[4:6] + "** **** " + card_num[-4:]
    else:
        logger.error(f"Неверный номер карты {card_num}")
        return 'Неверный формат номера карты'


logger.info("Запрос номера счета")


def get_mask_account(bill_num: str) -> str:
    """Возвращает маску номера счета по правилу **XXXX"""
    if len(bill_num) == 20 and bill_num.isdigit():
        logger.info("Вывод маскированного номера счета")
        return "**" + bill_num[-4:]
    else:
        logger.error(f"Неверный номер счета {bill_num}")
        return 'Неверный формат номера счета'


if __name__ == '__main__':
    print(get_mask_card_number('7000792289606361'))  #7000792289606361
    print(get_mask_account('73654108430135874305'))  #73654108430135874305
