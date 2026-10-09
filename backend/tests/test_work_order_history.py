
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.database import DATABASE_URL
from app.models import Base, Client, Employee, Vehicle, WorkOrder
from app.work_orders import list_vehicle_work_orders

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


def test_list_vehicle_work_orders(session):
    employee = Employee(
        name="João",
        email="joao@example.com",
        password_hash="hashed-password",
    )
    client = Client(name="Maria", phone="53999999999")
    other_client = Client(name="Pedro", phone="53888888888")
    session.add_all([employee, client, other_client])
    session.flush()

    vehicle = Vehicle(
        client_id=client.id,
        plate="ABC1D23",
        brand="Volkswagen",
        model="Gol",
        year=2020,
        mileage=50000,
    )
    other_vehicle = Vehicle(
        client_id=other_client.id,
        plate="XYZ9Z99",
        brand="Fiat",
        model="Uno",
        year=2018,
        mileage=60000,
    )
    session.add_all([vehicle, other_vehicle])
    session.flush()

    work_order = WorkOrder(
        vehicle_id=vehicle.id,
        initial_analysis="Motor fazendo barulho",
        services_performed="Troca de óleo",
        labor_cost=150,
        total=150,
        status="Finalizada",
        created_by=employee.id,
    )
    other_work_order = WorkOrder(
        vehicle_id=other_vehicle.id,
        initial_analysis="Falha no motor",
        services_performed="Diagnóstico",
        labor_cost=100,
        total=100,
        status="Em andamento",
        created_by=employee.id,
    )
    session.add_all([work_order, other_work_order])
    session.flush()

    results = list_vehicle_work_orders(session, vehicle.id)

    assert len(results) == 1
    assert results[0].id == work_order.id
    assert results[0].status == "Finalizada"