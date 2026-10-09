
from decimal import Decimal

from app.models import WorkOrderPart


def test_work_order_part_stores_historical_price():
    item = WorkOrderPart(
        work_order_id=1,
        part_id=1,
        quantity=2,
        unit_price=Decimal("35.90"),
    )

    assert item.work_order_id == 1
    assert item.part_id == 1
    assert item.quantity == 2
    assert item.unit_price == Decimal("35.90")