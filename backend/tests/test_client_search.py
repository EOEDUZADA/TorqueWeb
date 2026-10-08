import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.clients import search_clients
from app.database import DATABASE_URL
from app.models import Base, Client

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


def test_search_client_by_name(session):
    client = Client(
        name="João da Silva",
        phone="53999999999",
    )

    session.add(client)
    session.commit()

    results = search_clients(
        session,
        "João",
    )

    assert len(results) == 1
    assert results[0].name == "João da Silva"


def test_search_client_by_phone(session):
    client = Client(
        name="Maria da Silva",
        phone="53888888888",
    )

    session.add(client)
    session.commit()

    results = search_clients(
        session,
        "53888888888",
    )

    assert len(results) == 1
    assert results[0].phone == "53888888888"