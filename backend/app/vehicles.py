from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Vehicle


def register_vehicle(
    session: Session,
    client_id: int,
    plate: str,
    brand: str,
    model: str,
    year: int,
    mileage: int,
) -> Vehicle:
    vehicle = Vehicle(
        client_id=client_id,
        plate=plate,
        brand=brand,
        model=model,
        year=year,
        mileage=mileage,
    )

    session.add(vehicle)

    return vehicle


def search_vehicles(
    session: Session,
    term: str,
) -> list[Vehicle]:
    statement = select(Vehicle).where(
        Vehicle.plate.ilike(f"%{term}%")
    )

    return list(session.scalars(statement).all())


def list_client_vehicles(
    session: Session,
    client_id: int,
) -> list[Vehicle]:
    statement = select(Vehicle).where(
        Vehicle.client_id == client_id
    )

    return list(session.scalars(statement).all())