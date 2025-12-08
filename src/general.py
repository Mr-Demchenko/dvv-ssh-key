from masks import *

def mask_account_card(description: str) -> str:
    """Функция возвращает описание карты/счета и маску"""
    index = -1
    num=0
    for letter in description:
        num += 1
        if letter == " ":
            index = num

    if index == -1:
        return "Error"

    number = description[index:]
    if len(number) == 16:
        return f"{description[:index+1]}{get_mask_card_number(number)}"
    elif len(number) == 20:
        return f"{description[:index+1]}{get_mask_account(number)}"

    return "Error"


def get_date(date: str) -> str:
    """Функция возвращает строковое продставление даты в формате ДД.ММ.ГГГГ"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"