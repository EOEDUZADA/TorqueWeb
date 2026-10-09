from decimal import Decimal

import pytest

from app.models import Part
from app.parts import update_part_stock


def create_part() -> Part:
    return Part(
        name="Filtro de óleo",
        code="FO-001",
        category="Filtros",
        price=Decimal("35.90"),
        quantity_available=10,
        active=True,
    )


def test_update_part_stock():
    part = create_part()

    update_part_stock(part, 15)

    assert part.quantity_available == 15


#Testa se a quantidade da peça é negativa
def test_update_part_stock_rejects_negative_quantity():
    part = create_part()

    with pytest.raises(ValueError, match="não pode ser negativa"):
        update_part_stock(part, -1)

    assert part.quantity_available == 10