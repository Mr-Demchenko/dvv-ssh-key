import os
from pathlib import Path
from typing import Any

import requests

EXCHANGE_RATES_API_URL = "https://api.apilayer.com/exchangerates_data/convert"


def load_env_file(file_path: str | None = None) -> None:
    """Получение данных API из файла .env"""
    env_path = Path(file_path) if file_path else Path(__file__).resolve().parents[1] / ".env"
    if not env_path.exists():
        return

    for line in env_path.read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip())


def get_transaction_amount_in_rub(transaction: dict[str, Any]) -> float:
    """Возвращаем полученные данные с сайта"""
    operation_amount = transaction.get("operationAmount", {})
    amount = float(operation_amount.get("amount", 0))
    currency = operation_amount.get("currency", {}).get("code")

    if currency == "RUB":
        return amount

    if currency in ("USD", "EUR"):
        load_env_file()
        api_key = os.getenv("EXCHANGE_RATES_API_KEY", "")
        response = requests.get(
            EXCHANGE_RATES_API_URL,
            headers={"apikey": api_key},
            params={"from": currency, "to": "RUB", "amount": amount},
            timeout=10,
        )
        response.raise_for_status()
        return float(response.json().get("result", 0))

    return amount
