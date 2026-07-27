import pytest
from src.classes import *

# Фикстуры для создания тестовых данных
@pytest.fixture
def sample_product():
    """Фикстура для создания тестового товара"""
    return Product("Ноутбук", "Мощный ноутбук для работы", 1500.50, 10)


@pytest.fixture
def sample_products():
    """Фикстура для создания списка тестовых товаров"""
    return [
        Product("Мышь", "Беспроводная мышь", 25.99, 50),
        Product("Клавиатура", "Механическая клавиатура", 89.99, 30),
        Product("Монитор", "27-дюймовый монитор", 299.99, 15)
    ]


@pytest.fixture
def sample_category(sample_products):
    """Фикстура для создания тестовой категории с товарами"""
    return Category(
        "Периферия",
        "Компьютерная периферия",
        sample_products
    )


@pytest.fixture
def empty_category():
    """Фикстура для создания пустой категории"""
    return Category("Пустая категория", "Нет товаров")


@pytest.fixture
def reset_category_counts():
    """Фикстура для сброса счетчиков категорий перед тестом"""
    Category.category_count = 0
    Category.product_count = 0
    yield
    # После теста можно опционально сбросить обратно
    Category.category_count = 0
    Category.product_count = 0


def test_product_initialization(sample_product):
    """Тест корректной инициализации объекта Product с использованием фикстуры"""
    assert sample_product.name == "Ноутбук"
    assert sample_product.description == "Мощный ноутбук для работы"
    assert sample_product.price == 1500.50
    assert sample_product.quantity == 10


def test_product_initialization_with_different_values():
    """Тест инициализации Product с разными значениями"""
    product = Product("Смартфон", "Новый смартфон", 999.99, 25)

    assert product.name == "Смартфон"
    assert product.description == "Новый смартфон"
    assert product.price == 999.99
    assert product.quantity == 25


def test_category_initialization(sample_category, sample_products):
    """Тест корректной инициализации объекта Category с использованием фикстуры"""
    assert sample_category.name == "Периферия"
    assert sample_category.description == "Компьютерная периферия"
    assert len(sample_category.products) == 3
    assert sample_category.products == sample_products


def test_category_initialization_without_products(empty_category):
    """Тест создания категории без товаров с использованием фикстуры"""
    assert empty_category.name == "Пустая категория"
    assert empty_category.description == "Нет товаров"
    assert len(empty_category.products) == 0


def test_category_count(reset_category_counts, sample_products):
    """Тест подсчета количества категорий с использованием фикстуры"""
    # Создаем несколько категорий
    cat1 = Category("Электроника", "Электронные устройства", sample_products[:1])
    cat2 = Category("Одежда", "Модная одежда")
    cat3 = Category("Книги", "Художественная литература")

    assert Category.category_count == 3
    assert cat1.category_count == 3
    assert cat2.category_count == 3
    assert cat3.category_count == 3


def test_product_count(reset_category_counts, sample_products):
    """Тест подсчета количества продуктов с использованием фикстуры"""
    category = Category(
        "Тестовая категория",
        "Описание",
        sample_products
    )

    assert Category.product_count == 3
    assert category.product_count == 3


def test_category_count_auto_increment(reset_category_counts):
    """Тест автоматического увеличения счетчика категорий"""
    assert Category.category_count == 0

    category1 = Category("Категория 1", "Описание 1")
    assert Category.category_count == 1

    category2 = Category("Категория 2", "Описание 2")
    assert Category.category_count == 2

    category3 = Category("Категория 3", "Описание 3")
    assert Category.category_count == 3


def test_product_count_auto_increment(reset_category_counts):
    """Тест автоматического увеличения счетчика продуктов"""
    assert Category.product_count == 0

    products1 = [
        Product("Товар1", "Описание1", 100, 5),
        Product("Товар2", "Описание2", 200, 3)
    ]
    category1 = Category("Категория 1", "Описание 1", products1)
    assert Category.product_count == 2

    products2 = [
        Product("Товар3", "Описание3", 300, 7),
        Product("Товар4", "Описание4", 400, 2),
        Product("Товар5", "Описание5", 500, 1)
    ]
    category2 = Category("Категория 2", "Описание 2", products2)
    assert Category.product_count == 5


def test_multiple_categories_with_products(reset_category_counts, sample_products):
    """Тест с несколькими категориями и товарами"""
    # Первая категория с 3 товарами
    cat1 = Category("Электроника", "Электронные устройства", sample_products)

    # Вторая категория с 2 товарами
    products2 = [
        Product("Футболка", "Хлопковая футболка", 19.99, 100),
        Product("Джинсы", "Синие джинсы", 49.99, 50)
    ]
    cat2 = Category("Одежда", "Модная одежда", products2)

    # Проверяем общее количество товаров
    assert Category.product_count == 5  # 3 + 2

    # Проверяем количество категорий
    assert Category.category_count == 2


def test_category_products_are_objects(sample_category):
    """Тест проверяет, что в списке товаров хранятся объекты Product"""
    for product in sample_category.products:
        assert isinstance(product, Product)


def test_category_initialization_with_products_param_optional(sample_products):
    """Тест опционального параметра products при инициализации"""
    # Явно передаем пустой список
    category1 = Category("Категория 1", "Описание 1", [])
    assert len(category1.products) == 0

    # Не передаем products (должен создаться пустой список)
    category2 = Category("Категория 2", "Описание 2")
    assert len(category2.products) == 0

    # Передаем список с товарами
    category3 = Category("Категория 3", "Описание 3", sample_products)
    assert len(category3.products) == 3


# Дополнительные фикстуры для более сложных сценариев
@pytest.fixture
def expensive_products():
    """Фикстура с дорогими товарами"""
    return [
        Product("iPhone 15", "Флагманский смартфон", 999.99, 10),
        Product("MacBook Pro", "Мощный ноутбук", 2499.99, 5),
        Product("iPad Pro", "Планшет для творчества", 1099.99, 8)
    ]


@pytest.fixture
def cheap_products():
    """Фикстура с дешевыми товарами"""
    return [
        Product("Чехол", "Силиконовый чехол", 9.99, 200),
        Product("Зарядка", "Блок питания", 19.99, 150),
        Product("Наушники", "Проводные наушники", 14.99, 100)
    ]


def test_different_category_types(expensive_products, cheap_products, reset_category_counts):
    """Тест с разными типами категорий"""
    premium_category = Category("Премиум", "Дорогие товары", expensive_products)
    budget_category = Category("Бюджет", "Дешевые товары", cheap_products)

    assert premium_category.name == "Премиум"
    assert budget_category.name == "Бюджет"
    assert Category.category_count == 2
    assert Category.product_count == 6  # 3 + 3

    # Проверяем цены в разных категориях
    assert premium_category.products[0].price > 100
    assert budget_category.products[0].price < 20