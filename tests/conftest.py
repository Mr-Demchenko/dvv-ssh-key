import pytest

# this is the file with fixtures for all project


@pytest.fixture
def number_list():
    return [1, 2, 3, 4, 5]


@pytest.fixture
def card_number():
    return "Card 1234567890123456"
