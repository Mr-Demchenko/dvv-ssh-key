import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize('test, expected', [
    ('1234567890123456', "1234 56** **** 3456"),
    ('123456789012345', "Error"),
    ('', "Error"),
    ('dfd', "Error")
])
def test_get_mask_card_number(test, expected):
    assert get_mask_card_number(test) == expected
    # with pytest.raises(ValueError) as :
    #    get_mask_card_number(23)


@pytest.mark.parametrize('test, expected', [
    ('12345678901234567890', '**7890'),
    ('1234567890123456789012', '**9012'),
    ('', 'Error'),
    ('123456789012345678901', 'Error'),
    ('1234567890', 'Error')
])
def test_get_mask_account(test, expected):
    assert get_mask_account(test) == expected
    # assert get_mask_account("12345678901234567890") == ""
    # assert get_mask_account("1234567890123456789012") == "**9012"
