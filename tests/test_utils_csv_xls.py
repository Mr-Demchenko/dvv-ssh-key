from unittest.mock import Mock, mock_open, patch

from src.utils_csv_xls import read_csv_file, read_xls_file


def test_read_csv_file_returns_transactions() -> None:
    """Тестируем чтение CSV-файла в список словарей."""
    file_data = "id,state,amount,currency\n1,EXECUTED,100,RUB\n2,CANCELED,20,USD\n"

    with patch("builtins.open", mock_open(read_data=file_data)) as mocked_file:
        result = read_csv_file("transactions.csv")

    mocked_file.assert_called_once_with("transactions.csv", encoding="utf-8", newline="")
    assert result == [
        {"id": "1", "state": "EXECUTED", "amount": "100", "currency": "RUB"},
        {"id": "2", "state": "CANCELED", "amount": "20", "currency": "USD"},
    ]


def test_read_csv_file_returns_empty_list_for_missing_file() -> None:
    """Тестируем возврат пустого списка, если CSV-файл не найден."""
    with patch("builtins.open", side_effect=FileNotFoundError):
        assert read_csv_file("missing.csv") == []


def test_read_xls_file_returns_transactions() -> None:
    """Тестируем чтение Excel-файла в список словарей."""
    expected_transactions = [
        {"id": 1, "state": "EXECUTED", "amount": 100, "currency_code": "RUB"},
        {"id": 2, "state": "CANCELED", "amount": 20, "currency_code": "USD"},
    ]
    mocked_frame = Mock()
    mocked_frame.to_dict.return_value = expected_transactions

    with patch("src.utils_csv_xls.pd.read_excel", return_value=mocked_frame) as mocked_read_excel:
        result = read_xls_file("transactions.xlsx")

    mocked_read_excel.assert_called_once_with("transactions.xlsx", header=1)
    mocked_frame.to_dict.assert_called_once_with(orient="records")
    assert result == expected_transactions


def test_read_xls_file_returns_empty_list_for_missing_file() -> None:
    """Тестируем возврат пустого списка, если Excel-файл не найден."""
    with patch("src.utils_csv_xls.pd.read_excel", side_effect=FileNotFoundError):
        assert read_xls_file("missing.xlsx") == []
