from inventory_report.product import Product


def test_create_product() -> None:
    produto_teste = Product(
        '1',
        'bala de morango',
        'fini',
        '10/06/2024',
        '10/09/2024',
        '666',
        'guardar longe de umidade'
    )

    assert produto_teste.id == '1'
    assert produto_teste.product_name == 'bala de morango'
    assert produto_teste.company_name == 'fini'
    assert produto_teste.manufacturing_date == '10/06/2024'
    assert produto_teste.expiration_date == '10/09/2024'
    assert produto_teste.serial_number == '666'
    assert produto_teste.storage_instructions == 'guardar longe de umidade'
