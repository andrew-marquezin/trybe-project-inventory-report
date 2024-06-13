from datetime import date
from collections import Counter

from inventory_report.inventory import Inventory


class SimpleReport:
    def __init__(self) -> None:
        self.data = list()

    def add_inventory(self, inventory: Inventory) -> None:
        self.data.append(inventory)

    def generate(self) -> str:
        products = [
            product for inventory in self.data for product in inventory.data
        ]

        closest_expiration = min(
            product.expiration_date
            for product in products
            if product.expiration_date > date.today().strftime("%Y-%m-%d")
        )

        oldest_manufacturing = min(
            product.manufacturing_date for product in products
        )

        contagem = Counter(product.company_name for product in products)

        most_common_manufacturer = contagem.most_common(1)[0][0]

        return (
            f"Oldest manufacturing date: {oldest_manufacturing}"
            f"Closest expiration date: {closest_expiration}"
            f"Company with the largest inventory: {most_common_manufacturer}"
        )
