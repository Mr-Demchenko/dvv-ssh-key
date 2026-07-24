from typing import Any

from src.processing import filter_by_state, process_bank_search, sort_by_date
from src.utils import read_json_file
from src.utils_csv_xls import read_csv_file, read_xls_file
from src.widget import get_date, mask_account_card

DATA_FILES = {
    "1": ("JSON", "data/operations.json", read_json_file),
    "2": ("CSV", "data/transactions.csv", read_csv_file),
    "3": ("XLSX", "data/transactions.xlsx", read_xls_file),
}
VALID_STATUSES = {"EXECUTED", "CANCELED", "PENDING"}


def get_operation_amount(transaction: dict[str, Any]) -> str:
    """Возвращает сумму операции из JSON, CSV или XLSX-транзакции."""
    operation_amount = transaction.get("operationAmount")
    if isinstance(operation_amount, dict):
        return str(operation_amount.get("amount", ""))
    return str(transaction.get("amount", ""))


def get_operation_currency(transaction: dict[str, Any]) -> str:
    """Возвращает валюту операции из JSON, CSV или XLSX-транзакции."""
    operation_amount = transaction.get("operationAmount")
    if isinstance(operation_amount, dict):
        currency = operation_amount.get("currency", {})
        if isinstance(currency, dict):
            return str(currency.get("code", ""))
    return str(transaction.get("currency_code") or transaction.get("currency") or "")


def print_transaction(transaction: dict[str, Any]) -> None:
    """Печатает одну банковскую операцию в пользовательском формате."""
    date = get_date(str(transaction.get("date", ""))[:10])
    description = transaction.get("description", "")
    amount = get_operation_amount(transaction)
    currency = get_operation_currency(transaction)
    sender = transaction.get("from")
    receiver = transaction.get("to")

    print(f"{date} {description}")
    if sender and receiver:
        print(f"{mask_account_card(str(sender))} -> {mask_account_card(str(receiver))}")
    elif receiver:
        print(mask_account_card(str(receiver)))
    print(f"Сумма: {amount} {currency}")
    print()


def ask_status() -> str:
    """Запрашивает у пользователя корректный статус операции."""
    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        status = input("Пользователь: ").upper()
        if status in VALID_STATUSES:
            print(f'Операции отфильтрованы по статусу "{status}"')
            return status
        print(f'Статус операции "{status}" недоступен.')


def main() -> None:
    """Запускает пользовательский сценарий работы с банковскими транзакциями."""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    file_choice = input("Пользователь: ")
    file_type, file_path, file_reader = DATA_FILES.get(file_choice, DATA_FILES["1"])
    print(f"Для обработки выбран {file_type}-файл.")

    transactions = file_reader(file_path)
    status = ask_status()
    filtered_transactions = filter_by_state(transactions, status)

    if input("Отсортировать операции по дате? Да/Нет\nПользователь: ").lower() == "да":
        sort_direction = input("Отсортировать по возрастанию или по убыванию?\nПользователь: ").lower()
        filtered_transactions = sort_by_date(filtered_transactions, "убыв" in sort_direction)

    if input("Выводить только рублевые транзакции? Да/Нет\nПользователь: ").lower() == "да":
        filtered_transactions = [
            transaction for transaction in filtered_transactions if get_operation_currency(transaction) == "RUB"
        ]

    search_question = "Отфильтровать список транзакций по определенному слову в описании? Да/Нет\nПользователь: "
    if input(search_question).lower() == "да":
        search = input("Введите слово для поиска в описании\nПользователь: ")
        filtered_transactions = process_bank_search(filtered_transactions, search)

    print("Распечатываю итоговый список транзакций...")
    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
    print()
    for transaction in filtered_transactions:
        print_transaction(transaction)


if __name__ == "__main__":
    main()
