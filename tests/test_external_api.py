from unittest.mock import Mock, patch

from external_api import get_transaction_amount_in_rub


def test_get_transaction_amount_in_rub_returns_rub_amount_without_api_call() -> None:
    transaction = {
        "operationAmount": {
            "amount": "31957.58",
            "currency": {"code": "RUB"},
        }
    }

    with patch("external_api.requests.get") as mock_get:
        result = get_transaction_amount_in_rub(transaction)

    assert result == 31957.58
    mock_get.assert_not_called()


def test_get_transaction_amount_in_rub_converts_usd_with_api() -> None:
    transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "USD"},
        }
    }
    mock_response = Mock()
    mock_response.json.return_value = {"result": 9000.0}
    mock_response.raise_for_status.return_value = None

    with patch.dict("os.environ", {"EXCHANGE_RATES_API_KEY": "test_key"}):
        with patch("external_api.requests.get", return_value=mock_response) as mock_get:
            result = get_transaction_amount_in_rub(transaction)

    assert result == 9000.0
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert",
        headers={"apikey": "test_key"},
        params={"from": "USD", "to": "RUB", "amount": 100.0},
        timeout=10,
    )
    mock_response.raise_for_status.assert_called_once()


def test_get_transaction_amount_in_rub_converts_eur_with_api() -> None:
    transaction = {
        "operationAmount": {
            "amount": "50",
            "currency": {"code": "EUR"},
        }
    }
    mock_response = Mock()
    mock_response.json.return_value = {"result": 5000.0}
    mock_response.raise_for_status.return_value = None

    with patch.dict("os.environ", {"EXCHANGE_RATES_API_KEY": "test_key"}):
        with patch("external_api.requests.get", return_value=mock_response):
            result = get_transaction_amount_in_rub(transaction)

    assert result == 5000.0
