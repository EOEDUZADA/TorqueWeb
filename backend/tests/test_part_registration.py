
from decimal import Decimal

from app.models import Part
from app.parts import register_part


def test_register_part():
    part = register_part(
        name="Filtro de óleo",
        code="FO-001",
        category="Filtros",
        price=Decimal("35.90"),
        quantity_available=10,
    )

    assert isinstance(part, Part)
    assert part.name == "Filtro de óleo"
    assert part.code == "FO-001"
    assert part.category == "Filtros"
    assert part.price == Decimal("35.90")
    assert part.quantity_available == 10
    assert part.active is True