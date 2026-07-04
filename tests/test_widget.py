import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize('test, expected', [
    ('Card 1234567890123456', "Card 1234 56** **** 3456"),
    ("I don't know", "Error"),
    ("New card 1234567890123456", "New card 1234 56** **** 3456"),
    ("", "Error")
])
def test_mask_account_card(test, expected):
    assert mask_account_card(test) == expected


@pytest.mark.parametrize('test, expected', [
    ("2026.11.12", "12.11.2026"),
    ("2024.02.01", "01.02.2024"),
    ('abc', 'Error'),
    ('2040_10_04', '04.10.2040'),
    ('', 'Error')
])
def test_get_date(test, expected):
    assert get_date(test) == expected
