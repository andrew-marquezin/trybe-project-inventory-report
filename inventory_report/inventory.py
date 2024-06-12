from inventory_report.product import Product


class Inventory:
    def __init__(self, data: list[Product] | None = None) -> None:
        self._data = [] if data is None else data

    @property
    def data(self) -> list[Product]:
        return self._data

    def add_data(self, data: list[Product]) -> None:
        for product in data:
            self._data.append(product)
