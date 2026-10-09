
from decimal import Decimal

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.database import DATABASE_URL
from app.models import Base, Client, Employee, Part, Vehicle, WorkOrder
from app.work_orders import add_part_to_work_order

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


def test_add_part_to_work_order_updates_stock_and_price(session):
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
        quantity_available=10,
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
        total=Decimal("150.00"),
        status="Em andamento",
        created_by=employee.id,
    )
    session.add(work_order)
    session.flush()

    item = add_part_to_work_order(
        session=session,
        work_order=work_order,
        part=part,
        quantity=2,
    )
    session.flush()

    assert item.quantity == 2
    assert item.unit_price == Decimal("35.90")
    assert part.quantity_available == 8