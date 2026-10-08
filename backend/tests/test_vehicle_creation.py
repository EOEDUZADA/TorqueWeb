import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.database import DATABASE_URL
from app.models import Base, Client, Vehicle
from app.vehicles import register_vehicle

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


def test_register_vehicle(session):
    client = Client(
        name="João da Silva",
        phone="53999999999",
    )

    session.add(client)
    session.flush()
    

    vehicle = register_vehicle(
        session=session,
        client_id=client.id,
        plate="ABC1D23",
        brand="Volkswagen",
        model="Gol",
        year=2020,
        mileage=50000,
    )
    

    assert vehicle.plate == "ABC1D23"
    assert vehicle.brand == "Volkswagen"
    assert vehicle.model == "Gol"
    assert vehicle.year == 2020
    assert vehicle.mileage == 50000
    assert vehicle.client_id == client.id