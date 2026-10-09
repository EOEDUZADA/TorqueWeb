from sqlalchemy import select

from decimal import Decimal

from sqlalchemy.orm import Session

from app.models import WorkOrder, Part, WorkOrderPart

from datetime import datetime, timezone


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


def list_work_orders(
    session: Session,
    page: int = 1,
    page_size: int = 10,
) -> list[WorkOrder]:
    if page < 1:
        raise ValueError("A página deve ser maior ou igual a 1")

    if page_size < 1:
        raise ValueError("O tamanho da página deve ser maior ou igual a 1")

    statement = (
        select(WorkOrder)
        .order_by(WorkOrder.id.desc())
        .offset((page - 1) * page_size)
        .limit(page_size)
    )

    return list(session.scalars(statement).all())


def add_part_to_work_order(
    session: Session,
    work_order: WorkOrder,
    part: Part,
    quantity: int,
) -> WorkOrderPart:
    if work_order.status != "Em andamento":
        raise ValueError("A ordem de serviço não está em andamento")

    if quantity <= 0:
        raise ValueError("A quantidade deve ser maior que zero")

    if not part.active:
        raise ValueError("A peça está inativa")

    if part.quantity_available < quantity:
        raise ValueError("Estoque insuficiente")

    item = WorkOrderPart(
        work_order_id=work_order.id,
        part_id=part.id,
        quantity=quantity,
        unit_price=part.price,
    )

    part.quantity_available -= quantity
    session.add(item)

    #Sem commit para caso houver falha poder ter rollback e não baixar o estoque 

    return item


def remove_part_from_work_order(
    session: Session,
    work_order: WorkOrder,
    item: WorkOrderPart,
) -> None:
    if work_order.status != "Em andamento":
        raise ValueError("A ordem de serviço não está em andamento")

    if item.work_order_id != work_order.id:
        raise ValueError("A peça não pertence a esta ordem de serviço")

    part = session.get(Part, item.part_id)

    if part is None:
        raise ValueError("Peça não encontrada")

    part.quantity_available += item.quantity
    session.delete(item)


def recalculate_work_order_total(
    work_order: WorkOrder,
    items: list[WorkOrderPart],
) -> None:
    parts_total = sum(
        (
            item.unit_price * item.quantity
            for item in items
        ),
        Decimal("0.00"),
    )

    work_order.total = work_order.labor_cost + parts_total


def edit_work_order(
    work_order: WorkOrder,
    initial_analysis: str,
    services_performed: str,
    labor_cost: Decimal,
) -> None:
    if work_order.status != "Em andamento":
        raise ValueError("A ordem de serviço finalizada não pode ser editada")

    if labor_cost < 0:
        raise ValueError("O custo da mão de obra não pode ser negativo")

    work_order.total += labor_cost - work_order.labor_cost
    work_order.initial_analysis = initial_analysis
    work_order.services_performed = services_performed
    work_order.labor_cost = labor_cost



def finish_work_order(
    work_order: WorkOrder,
    employee_id: int,
) -> None:
    if work_order.status == "Finalizada":
        raise ValueError("A ordem de serviço já está finalizada")

    work_order.status = "Finalizada"
    work_order.finished_by = employee_id
    work_order.finished_at = datetime.now(timezone.utc)


def list_vehicle_work_orders(
    session: Session,
    vehicle_id: int,
) -> list[WorkOrder]:
    statement = (
        select(WorkOrder)
        .where(WorkOrder.vehicle_id == vehicle_id)
        .order_by(WorkOrder.id.desc())
    )

    return list(session.scalars(statement).all())