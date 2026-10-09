
from decimal import Decimal

import pytest

from app.models import WorkOrder
from app.work_orders import edit_work_order


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


def test_edit_work_order():
    work_order = create_work_order()

    edit_work_order(
        work_order=work_order,
        initial_analysis="Motor com ruído na partida",
        services_performed="Troca de óleo e filtro",
        labor_cost=Decimal("180.00"),
    )

    assert work_order.initial_analysis == "Motor com ruído na partida"
    assert work_order.services_performed == "Troca de óleo e filtro"
    assert work_order.labor_cost == Decimal("180.00")


def test_cannot_edit_finished_work_order():
    work_order = create_work_order(status="Finalizada")

    with pytest.raises(ValueError, match="finalizada"):
        edit_work_order(
            work_order=work_order,
            initial_analysis="Nova análise",
            services_performed="Novo serviço",
            labor_cost=Decimal("200.00"),
        )

    assert work_order.initial_analysis == "Motor fazendo barulho"
    assert work_order.labor_cost == Decimal("150.00")


def test_cannot_set_negative_labor_cost():
    work_order = create_work_order()

    with pytest.raises(ValueError, match="negativo"):
        edit_work_order(
            work_order=work_order,
            initial_analysis="Nova análise",
            services_performed="Novo serviço",
            labor_cost=Decimal("-1.00"),
        )

    assert work_order.labor_cost == Decimal("150.00")