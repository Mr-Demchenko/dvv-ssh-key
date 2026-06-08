def filter_by_currency(transactions: list, currency: str):
    """Функция принимает список транзакций и код валюты, а возвращает итератор с транзакциями в указанной валюте."""
    filter_list = filter(lambda s: s["operationAmount"]["currency"]["code"] == currency, transactions, )

    for next_elem in filter_list:
        yield next_elem


def transaction_descriptions(transactions: list) -> str:
    """Функция принимает список транзакций и по очереди возвращает описание каждой операции."""
    for next_elem in transactions:
        yield next_elem.descriptions


def card_number_generator(fist_num: int, last_num: int) -> str:
    """Функция `card_number_generator` принимает начальное и конечное значения диапазона и генерирует номера карт в
    формате `XXXX XXXX XXXX XXXX`"""
    card_list = [x for x in range(fist_num, last_num)]
    for num in card_list:
        str_num = "0000000000000000"+str(num)
        str_num = str_num[len(str_num)-16:len(str_num)]
        yield f"{str_num[0:4]} {str_num[4:8]} {str_num[8:12]} {str_num[12:16]}"
