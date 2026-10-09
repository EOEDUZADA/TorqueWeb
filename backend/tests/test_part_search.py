
from decimal import Decimal

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.database import DATABASE_URL
from app.models import Base, Part
from app.parts import search_parts

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


def test_search_part_by_name(session):
    part = Part(
        name="Filtro de óleo",
        code="FO-001",
        category="Filtros",
        price=Decimal("35.90"),
        quantity_available=10,
        active=True,
    )

    session.add(part)
    session.flush()

    results = search_parts(session, "Filtro")

    assert len(results) == 1
    assert results[0].name == "Filtro de óleo"


def test_search_part_by_code(session):
    part = Part(
        name="Filtro de óleo",
        code="FO-001",
        category="Filtros",
        price=Decimal("35.90"),
        quantity_available=10,
        active=True,
    )

    session.add(part)
    session.flush()

    results = search_parts(session, "FO-001")

    assert len(results) == 1
    assert results[0].code == "FO-001"