import json


class Product:

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:

    category_count = 0
    product_count = 0

    def __init__(
        self,
        name: str,
        description: str,
        products: list[Product] | None = None,
    ):
        self.name = name
        self.description = description
        self.products = products if products is not None else []

        Category.category_count += 1
        Category.product_count += len(self.products)


def load_category_from_json(file_name: str) -> list:
    with open(file_name, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    categories = []

    for category_data in data:
        products = []

        for product_data in category_data.get('products', []):
            products.append(
                Product(
                    product_data.get('name'),
                    product_data.get('description'),
                    product_data.get('price'),
                    product_data.get('quantity'),
                )
            )

        categories.append(
            Category(
                category_data.get('name'),
                category_data.get('description'),
                products,
            )
        )

    return categories
