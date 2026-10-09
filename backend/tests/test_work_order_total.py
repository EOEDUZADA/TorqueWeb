
from decimal import Decimal

from app.models import WorkOrder, WorkOrderPart
from app.work_orders import recalculate_work_order_total


def test_recalculate_work_order_total():
    work_order = WorkOrder(
        vehicle_id=1,
        initial_analysis="Motor fazendo barulho",
        services_performed="Troca de óleo",
        labor_cost=Decimal("150.00"),
        total=Decimal("150.00"),
        status="Em andamento",
        created_by=1,
    )

    items = [
        WorkOrderPart(
            work_order_id=1,
            part_id=1,
            quantity=2,
            unit_price=Decimal("35.90"),
        ),
        WorkOrderPart(
            work_order_id=1,
            part_id=2,
            quantity=1,
            unit_price=Decimal("20.00"),
        ),
    ]

    recalculate_work_order_total(work_order, items)

    assert work_order.total == Decimal("241.80")