
from datetime import datetime, timezone
from decimal import Decimal

import pytest

from app.models import WorkOrder
from app.work_orders import finish_work_order


def create_work_order(status="Em andamento"):
    return WorkOrder(
        vehicle_id=1,
        initial_analysis="Motor fazendo barulho",
        services_performed="Troca de óleo",
        labor_cost=Decimal("150.00"),
        total=Decimal("150.00"),
        status=status,
        created_by=1,
    )


def test_finish_work_order():
    work_order = create_work_order()

    finish_work_order(work_order, employee_id=2)

    assert work_order.status == "Finalizada"
    assert work_order.finished_by == 2
    assert isinstance(work_order.finished_at, datetime)
    assert work_order.finished_at.tzinfo is not None


def test_cannot_finish_already_finished_work_order():
    work_order = create_work_order(status="Finalizada")

    with pytest.raises(ValueError, match="finalizada"):
        finish_work_order(work_order, employee_id=2)