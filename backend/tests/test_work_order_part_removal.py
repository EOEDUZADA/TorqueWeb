
from decimal import Decimal

import pytest
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from app.database import DATABASE_URL
from app.models import (
    Base,
    Client,
    Employee,
    Part,
    Vehicle,
    WorkOrder,
    WorkOrderPart,
)
from app.work_orders import remove_part_from_work_order

engine = create_engine(DATABASE_URL)


@pytest.fixture
def session():
    Base.metadata.create_all(engine)
    connection = engine.connect()
    transaction = connection.begin()
    session = Session(bind=connection)

    try:
        yield session
    finally:
        session.close()
        transaction.rollback()
        connection.close()


def test_remove_part_restores_stock(session):
    employee = Employee(
        name="João",
        email="joao@example.com",
        password_hash="hashed-password",
    )
    client = Client(name="Maria", phone="53999999999")
    part = Part(
        name="Filtro de óleo",
        code="FO-001",
        category="Filtros",
        price=Decimal("35.90"),
        quantity_available=8,
        active=True,
    )
    session.add_all([employee, client, part])
    session.flush()

    vehicle = Vehicle(
        client_id=client.id,
        plate="ABC1D23",
        brand="Volkswagen",
        model="Gol",
        year=2020,
        mileage=50000,
    )
    session.add(vehicle)
    session.flush()

    work_order = WorkOrder(
        vehicle_id=vehicle.id,
        initial_analysis="Motor fazendo barulho",
        services_performed="Troca de óleo",
        labor_cost=Decimal("150.00"),
        total=Decimal("221.80"),
        status="Em andamento",
        created_by=employee.id,
    )
    session.add(work_order)
    session.flush()

    item = WorkOrderPart(
        work_order_id=work_order.id,
        part_id=part.id,
        quantity=2,
        unit_price=Decimal("35.90"),
    )
    session.add(item)
    session.flush()

    remove_part_from_work_order(
        session=session,
        work_order=work_order,
        item=item,
    )
    session.flush()

    remaining_item = session.scalars(
        select(WorkOrderPart).where(
            WorkOrderPart.id == item.id
        )
    ).first()

    assert part.quantity_available == 10
    assert remaining_item is None