import pytest

from inventory_report.product import Product


def test_product_report(capsys: pytest.CaptureFixture) -> None:
    farinha = Product(
        '2',
        'farinha',
        'Farinini',
        '01-05-2021',
        '02-06-2023',
        'TY68 409C JJ43 ASD1 PL2F',
        'precisa ser armazenado em local protegido da luz'
    )
    print(str(farinha))

    captured = capsys.readouterr()

    assert captured.out == (
            f"The product {farinha.id} - {farinha.product_name} "
            f"with serial number {farinha.serial_number} "
            f"manufactured on {farinha.manufacturing_date} "
            f"by the company {farinha.company_name} "
            f"valid until {farinha.expiration_date} "
            "must be stored according to the following instructions: "
            f"{farinha.storage_instructions}.\n"
    )
