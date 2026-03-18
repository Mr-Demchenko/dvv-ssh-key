import pytest

from utils.code import calculate_logarithm, up_fist


def test_up_first():
    assert up_fist('skypro') == 'Skypro'


def test_up_first_for_empty():
    assert up_fist('') == ''


def test_calculate_logarithm_with_negative_number():
    with pytest.raises(ValueError) as exc_info:
        calculate_logarithm(-1)

    # Проверяем, что сообщение об ошибке соответствует ожидаемому
    assert str(exc_info.value) == "Логарифм можно вычислить только для положительных чисел"
