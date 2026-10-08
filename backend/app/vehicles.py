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