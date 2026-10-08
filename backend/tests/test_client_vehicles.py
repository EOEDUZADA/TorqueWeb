import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.database import DATABASE_URL
from app.models import Base, Client, Vehicle
from app.vehicles import list_client_vehicles

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


def test_list_client_vehicles(session):
    client = Client(
        name="João da Silva",
        phone="53999999999",
    )

    other_client = Client(
        name="Maria da Silva",
        phone="53888888888",
    )

    session.add_all([client, other_client])
    session.flush()

    vehicle_1 = Vehicle(
        client_id=client.id,
        plate="ABC1D23",
        brand="Volkswagen",
        model="Gol",
        year=2020,
        mileage=50000,
    )

    vehicle_2 = Vehicle(
        client_id=client.id,
        plate="DEF4G56",
        brand="Fiat",
        model="Uno",
        year=2018,
        mileage=70000,
    )

    other_vehicle = Vehicle(
        client_id=other_client.id,
        plate="HIJ7K89",
        brand="Chevrolet",
        model="Onix",
        year=2022,
        mileage=30000,
    )

    session.add_all([
        vehicle_1,
        vehicle_2,
        other_vehicle,
    ])

    session.flush()

    results = list_client_vehicles(
        session,
        client.id,
    )

    assert len(results) == 2
    assert results[0].client_id == client.id
    assert results[1].client_id == client.id