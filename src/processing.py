import re
from collections import Counter


def filter_by_state(list_of_dict: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """Функция получает на вход список словарей и возвращает список по условию значение state"""
    result_list = list()
    for element in list_of_dict:
        for key, value in element.items():
            if (key == 'state') & (value == state):
                result_list.append(element)
    return result_list


def sort_by_date(list_of_dict: list[dict], need_reverse: bool = True) -> list[dict]:
    """Функция получает на вход список словарей возвращает отсортированный по дате список"""
    return sorted(list_of_dict, key=lambda s_date: s_date['date'], reverse=need_reverse)


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Возвращает операции, у которых в описании есть строка поиска."""
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    return [transaction for transaction in data if pattern.search(str(transaction.get('description', '')))]


def process_bank_operations(data: list[dict], categories: list[str]) -> dict[str, int]:
    """Считает количество операций по категориям из поля description."""
    descriptions = [transaction.get('description') for transaction in data]
    counter = Counter(descriptions)
    return {category: counter[category] for category in categories}
