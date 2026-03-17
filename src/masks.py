def get_mask_card_number(card_number: str) -> str:
    """Функция возвращает маску номера карт по маске"""
    if len(card_number) != 16:
        return "Error"

    return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Функция возвращает маску номера счета по маске"""
    if not (len(account_number) == 20 or len(account_number) == 22):
        return "Error"

    return f"**{account_number[-4:]}"



#'1234567890123456' == '1234 56** **** 3456'
print(get_mask_card_number('1234567890123456'))
print(get_mask_card_number('123456789012345'))