from app.models import Part


def test_part_model():
    part = Part(
        name="Filtro de óleo",
        code="FO-001",
        category="Filtros",
        price=35.90,
        quantity_available=10,
        active=True, #Indica se a peça está em estoque
    )

    assert part.name == "Filtro de óleo"
    assert part.code == "FO-001"
    assert part.category == "Filtros"
    assert part.price == 35.90
    assert part.quantity_available == 10
    assert part.active is True