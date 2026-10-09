
from decimal import Decimal

from sqlalchemy.orm import Session

from app.models import WorkOrder


def create_work_order(
    session: Session,
    vehicle_id: int,
    initial_analysis: str,
    services_performed: str,
    labor_cost: Decimal,
    created_by: int,
) -> WorkOrder:
    work_order = WorkOrder(
        vehicle_id=vehicle_id,
        initial_analysis=initial_analysis,
        services_performed=services_performed,
        labor_cost=labor_cost,
        total=labor_cost,
        status="Em andamento",
        created_by=created_by,
    )

    session.add(work_order)
    return work_order