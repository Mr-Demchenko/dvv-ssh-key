from collections.abc import Iterator

import pytest

from generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)


@pytest.fixture
def currency_transactions() -> list[dict]:
    return [
        {
            "id": 1,
            "operationAmount": {"currency": {"code": "USD"}},
        },
        {
            "id": 2,
            "operationAmount": {"currency": {"code": "RUB"}},
        },
        {
            "id": 3,
            "operationAmount": {"currency": {"code": "USD"}},
        },
    ]


@pytest.fixture
def description_transactions() -> list[dict[str, str]]:
    return [
        {"description": "Перевод организации"},
        {"description": "Открытие вклада"},
        {"description": "Перевод с карты на карту"},
    ]


@pytest.fixture
def expected_descriptions() -> list[str]:
    return [
        "Перевод организации",
        "Открытие вклада",
        "Перевод с карты на карту",
    ]


@pytest.fixture
def expected_card_numbers() -> list[str]:
    return [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
    ]


def test_filter_by_currency_returns_iterator(currency_transactions: list[dict]):
    result = filter_by_currency(currency_transactions, "USD")

    assert isinstance(result, Iterator)


def test_filter_by_currency_filters_transactions_by_currency_code(currency_transactions: list[dict]):
    result = list(filter_by_currency(currency_transactions, "USD"))

    assert result == [currency_transactions[0], currency_transactions[2]]


def test_transaction_descriptions_returns_iterator(description_transactions: list[dict[str, str]]):
    result = transaction_descriptions(description_transactions)

    assert isinstance(result, Iterator)


def test_transaction_descriptions_yields_descriptions_in_order(description_transactions: list[dict],
                                                               expected_descriptions: list[str],):
    result = list(transaction_descriptions(description_transactions))

    assert result == expected_descriptions


def test_card_number_generator_returns_iterator():
    result = card_number_generator(1, 1)

    assert isinstance(result, Iterator)


def test_card_number_generator_formats_cards_in_range(expected_card_numbers: list[str],):
    result = list(card_number_generator(1, 3))

    assert result == expected_card_numbers


def test_card_number_generator_includes_end_value():
    result = list(card_number_generator(9999999999999998, 9999999999999999))

    assert result == [
        "9999 9999 9999 9998",
        "9999 9999 9999 9999",
    ]
