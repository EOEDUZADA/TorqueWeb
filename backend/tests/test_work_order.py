
from decimal import Decimal

from app.models import WorkOrder


def test_work_order_model():
    work_order = WorkOrder(
        vehicle_id=1,
        initial_analysis="Motor fazendo barulho",
        services_performed="Troca de óleo",
        labor_cost=Decimal("150.00"),
        total=Decimal("150.00"),
        status="Em andamento",
        created_by=1,
    )

    assert work_order.vehicle_id == 1
    assert work_order.initial_analysis == "Motor fazendo barulho"
    assert work_order.services_performed == "Troca de óleo"
    assert work_order.labor_cost == Decimal("150.00")
    assert work_order.total == Decimal("150.00")
    assert work_order.status == "Em andamento"
    assert work_order.created_by == 1