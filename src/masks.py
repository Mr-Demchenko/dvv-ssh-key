import logging
from pathlib import Path

logger_masks = logging.getLogger('masks')
logger_masks.setLevel(logging.DEBUG)

project_root = Path(__file__).resolve().parents[1]
logs_dir = project_root / "logs"
logs_dir.mkdir(exist_ok=True)

file_handler = logging.FileHandler(logs_dir / "masks.log", encoding="utf-8")
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger_masks.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция возвращает маску номера карт по маске"""
    if len(card_number) != 16:
        logger_masks.error(f'Error of length card number {card_number} not 16')
        return "Error"

    result = f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    logger_masks.info(f'Return {result}')
    return result


def get_mask_account(account_number: str) -> str:
    """Функция возвращает маску номера счета по маске"""
    if not (len(account_number) == 20 or len(account_number) == 22):
        logger_masks.error(f'Error of length account number {account_number} not 20 and not 22')
        return "Error"

    result = f"**{account_number[-4:]}"
    logger_masks.info(f'Return {result}')
    return result
