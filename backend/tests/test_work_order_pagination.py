
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.database import DATABASE_URL
from app.models import Base, Client, Employee, Vehicle, WorkOrder
from app.work_orders import list_work_orders

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


def test_list_work_orders_paginates(session):
    employee = Employee(
        name="João",
        email="joao@example.com",
        password_hash="hashed-password",
    )
    client = Client(name="Maria", phone="53999999999")
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

    for index in range(12):
        session.add(
            WorkOrder(
                vehicle_id=vehicle.id,
                initial_analysis=f"Problema {index}",
                services_performed="Diagnóstico",
                labor_cost=100,
                total=100,
                status="Em andamento",
                created_by=employee.id,
            )
        )

    session.flush()

    first_page = list_work_orders(session, page=1, page_size=10)
    second_page = list_work_orders(session, page=2, page_size=10)

    assert len(first_page) == 10
    assert len(second_page) == 2
    assert set(item.id for item in first_page).isdisjoint(
        item.id for item in second_page
    )