import json
from typing import Any


def read_json_file(file_path: str) -> list[dict[str, Any]]:
    """Получаем JSON из файла и переводим в список словарей"""
    try:
        with open(file_path, encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

    if not isinstance(data, list):
        return []

    return data
