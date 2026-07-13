import json
from pathlib import Path
from unittest.mock import mock_open, patch

from src.utils import read_json_file


def test_read_json_file_returns_transactions(tmp_path: Path) -> None:
    transactions = [
        {"id": 1, "operationAmount": {"amount": "100", "currency": {"code": "RUB"}}},
        {"id": 2, "operationAmount": {"amount": "20", "currency": {"code": "USD"}}},
    ]
    file_path = tmp_path / "operations.json"
    file_path.write_text(json.dumps(transactions), encoding="utf-8")

    assert read_json_file(str(file_path)) == transactions


def test_read_json_file_returns_empty_list_for_missing_file() -> None:
    with patch("builtins.open", side_effect=FileNotFoundError):
        assert read_json_file("missing.json") == []


def test_read_json_file_returns_empty_list_for_empty_file(tmp_path: Path) -> None:
    file_path = tmp_path / "empty.json"
    file_path.write_text("", encoding="utf-8")

    assert read_json_file(str(file_path)) == []


def test_read_json_file_returns_empty_list_for_not_list_json() -> None:
    file_data = '{"id": 1}'

    with patch("builtins.open", mock_open(read_data=file_data)):
        assert read_json_file("operations.json") == []
