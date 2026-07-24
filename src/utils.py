import json
import logging
from pathlib import Path
from typing import Any

logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)

project_root = Path(__file__).resolve().parents[1]
logs_dir = project_root / "logs"
logs_dir.mkdir(exist_ok=True)

file_handler = logging.FileHandler(logs_dir / "utils.log", encoding="utf-8")
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_json_file(file_path: str) -> list[dict[str, Any]]:
    """Получаем JSON из файла и переводим в список словарей"""
    try:
        with open(file_path, encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as error_str:
        logger.error(f'{error_str}')
        return []

    if not isinstance(data, list):
        logger.info('Empty data')
        return []

    logger.info('data returning is ok')
    return data
