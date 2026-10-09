
from decimal import Decimal

from app.models import Part
from app.parts import is_part_available


def test_part_with_stock_is_available():
    part = Part(
        name="Filtro de óleo",
        code="FO-001",
        category="Filtros",
        price=Decimal("35.90"),
        quantity_available=10,
        active=True,
    )

    assert is_part_available(part) is True


def test_part_without_stock_is_unavailable():
    part = Part(
        name="Filtro de óleo",
        code="FO-001",
        category="Filtros",
        price=Decimal("35.90"),
        quantity_available=0,
        active=True,
    )

    assert is_part_available(part) is False