import csv
import logging
from pathlib import Path
from typing import Any

import pandas as pd

logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)

project_root = Path(__file__).resolve().parents[1]
logs_dir = project_root / "logs"
logs_dir.mkdir(exist_ok=True)

file_handler = logging.FileHandler(logs_dir / "utils_csv_xls.log", encoding="utf-8")
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_csv_file(file_path: str) -> list[dict[str, Any]]:
    """Получаем CSV из файла и переводим в список словарей."""
    try:
        with open(file_path, encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError as error_str:
        logger.error(f'{error_str}')
        return []


def read_xls_file(file_path: str) -> list[dict[str, Any]]:
    """Получаем XLS из файла и переводим в список словарей."""
    try:
        reader = pd.read_excel(file_path, header=1)
        return reader.to_dict(orient="records")
    except FileNotFoundError as error_str:
        logger.error(f'{error_str}')
        return []
