# Проект Банковское приложение

## Описание

Проект содержит функции для обработки банковских карт, счетов и финансовых операций.

Возможности проекта:

- маскировка номеров банковских карт и счетов;
- фильтрация операций по статусу;
- сортировка операций по дате;
- генерация номеров банковских карт;
- фильтрация транзакций по валюте;
- получение описаний транзакций;
- чтение финансовых операций из JSON-файла;
- чтение финансовых операций из CSV-файла;
- чтение финансовых операций из Excel-файла;
- конвертация сумм операций из USD и EUR в рубли через Exchange Rates Data API;
- логирование работы функций.

## Установка

1. Клонируйте репозиторий:

```bash
git clone git@github.com:Mr-Demchenko/dvv-ssh-key.git
```

2. Установите зависимости через Poetry:

```bash
poetry install
```

3. Создайте файл `.env` на основе `.env.example` и добавьте API-ключ:

```text
EXCHANGE_RATES_API_KEY=ваш_ключ_api
```

Файл `.env` не должен попадать в репозиторий.

## Зависимости

Основные библиотеки проекта:

- `requests` - запросы к внешнему API для конвертации валют;
- `python-dotenv` - работа с переменными окружения;
- `pandas` - чтение и обработка табличных данных;
- `openpyxl` - чтение Excel-файлов `.xlsx`;
- `pytest` и `pytest-cov` - тестирование и проверка покрытия.

## Использование

### Чтение JSON

```python
from src.utils import read_json_file

transactions = read_json_file("data/operations.json")
```

Функция возвращает список словарей с финансовыми операциями. Если файл не найден, пустой или содержит данные не в формате списка, возвращается пустой список.

### Чтение CSV

```python
from src.utils_csv_xls import read_csv_file

transactions = read_csv_file("data/transactions.csv")
```

Функция принимает путь к CSV-файлу и возвращает список словарей, где ключи берутся из заголовков CSV.

### Чтение Excel

```python
from src.utils_csv_xls import read_xls_file

transactions = read_xls_file("data/transactions.xlsx")
```

Функция принимает путь к Excel-файлу и возвращает список словарей с финансовыми операциями.

### Конвертация валюты

```python
from src.external_api import get_transaction_amount_in_rub

amount = get_transaction_amount_in_rub(transaction)
```

Если операция выполнена в рублях, функция возвращает сумму операции как `float`.
Если операция выполнена в USD или EUR, функция обращается к Exchange Rates Data API и возвращает сумму в рублях.

### Генераторы

Модуль `generators.py` содержит:

- `filter_by_currency` - фильтрует транзакции по валюте;
- `transaction_descriptions` - возвращает описания операций по очереди;
- `card_number_generator` - генерирует номера карт в формате `XXXX XXXX XXXX XXXX`.

## Тестирование

Запуск тестов:

```bash
poetry run pytest
```

Запуск тестов с покрытием:

```bash
poetry run pytest --cov=src --cov-report=term-missing
```

Проверка стиля кода:

```bash
poetry run flake8
```

Проверка сортировки импортов:

```bash
poetry run isort --check-only .
```

## Лицензия

Этот проект лицензирован по лицензии MIT.
