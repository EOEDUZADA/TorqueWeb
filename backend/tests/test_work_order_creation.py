
from decimal import Decimal

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.database import DATABASE_URL
from app.models import Base, Client, Employee, Vehicle, WorkOrder
from app.work_orders import create_work_order

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


def test_create_work_order(session):
    employee = Employee(
        name="João",
        email="joao@example.com",
        password_hash="hashed-password",
    )
    client = Client(
        name="Maria da Silva",
        phone="53999999999",
    )
    session.add_all([employee, client])
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

    work_order = create_work_order(
        session=session,
        vehicle_id=vehicle.id,
        initial_analysis="Motor fazendo barulho",
        services_performed="Troca de óleo",
        labor_cost=Decimal("150.00"),
        created_by=employee.id,
    )

    session.flush()

    assert work_order.id is not None
    assert work_order.vehicle_id == vehicle.id
    assert work_order.initial_analysis == "Motor fazendo barulho"
    assert work_order.services_performed == "Troca de óleo"
    assert work_order.labor_cost == Decimal("150.00")
    assert work_order.total == Decimal("150.00")
    assert work_order.status == "Em andamento"
    assert work_order.created_by == employee.id