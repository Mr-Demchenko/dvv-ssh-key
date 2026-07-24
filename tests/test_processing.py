import pytest

from src.processing import filter_by_state, process_bank_operations, process_bank_search, sort_by_date


@pytest.mark.parametrize('test, execute', [
    ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
      {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}],
     [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
      {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
     )
])
def test_filter_by_state(test, execute):
    assert filter_by_state(test) == execute


@pytest.mark.parametrize('test, execute', [
    ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
      {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
      {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
     [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
      {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
      {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
     )
])
def test_sort_by_date(test, execute):
    assert sort_by_date(test) == execute


def test_process_bank_search_returns_operations_by_description():
    transactions = [
        {'description': 'Перевод организации', 'state': 'EXECUTED'},
        {'description': 'Открытие вклада', 'state': 'EXECUTED'},
        {'description': 'Перевод с карты на карту', 'state': 'CANCELED'},
        {'state': 'EXECUTED'},
    ]

    result = process_bank_search(transactions, 'перевод')

    assert result == [transactions[0], transactions[2]]


def test_process_bank_search_returns_empty_list_without_matches():
    transactions = [
        {'description': 'Перевод организации', 'state': 'EXECUTED'},
        {'description': 'Открытие вклада', 'state': 'EXECUTED'},
    ]

    assert process_bank_search(transactions, 'наличные') == []


def test_process_bank_operations_counts_categories():
    transactions = [
        {'description': 'Перевод организации'},
        {'description': 'Открытие вклада'},
        {'description': 'Перевод организации'},
        {'description': 'Перевод с карты на карту'},
    ]
    categories = ['Перевод организации', 'Открытие вклада', 'Перевод со счета на счет']

    assert process_bank_operations(transactions, categories) == {
        'Перевод организации': 2,
        'Открытие вклада': 1,
        'Перевод со счета на счет': 0,
    }
