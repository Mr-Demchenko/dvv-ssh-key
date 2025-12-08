from masks import *

def mask_account_card(description_account: str) -> str:
    """Функция возвращает описание карты/счета и маску"""
    index = -1
    num=0
    for letter in description_account:
        num += 1
        if letter == " ":
            index = num

    if index == -1:
        return "Error"

    number_account = description_account[index:]
    if len(number_account) == 16:
        return f"{description_account[:index+1]}{get_mask_card_number(number_account)}"
    elif len(number_account) == 20:
        return f"{description_account[:index+1]}{get_mask_account(number_account)}"

    return "Error"


def get_date(date_string: str) -> str:
    """Функция возвращает строковое продставление даты в формате ДД.ММ.ГГГГ"""
    return f"{date_string[8:10]}.{date_string[5:7]}.{date_string[0:4]}"