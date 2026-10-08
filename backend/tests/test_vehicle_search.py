import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.database import DATABASE_URL
from app.models import Base, Client, Vehicle
from app.vehicles import search_vehicles

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


def test_search_vehicle_by_plate(session):
    client = Client(
        name="João da Silva",
        phone="53999999999",
    )

    session.add(client)
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

    results = search_vehicles(
        session,
        "ABC1D23",
    )

    assert len(results) == 1
    assert results[0].plate == "ABC1D23"