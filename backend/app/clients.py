from app.models import Client
from sqlalchemy import select
from sqlalchemy.orm import Session


def register_client(
    name: str,
    phone: str,
) -> Client:
    return Client(
        name=name,
        phone=phone,
    )


def search_clients(
    session: Session,
    term: str,
) -> list[Client]:
    statement = select(Client).where(
        (Client.name.ilike(f"%{term}%"))
        | (Client.phone.ilike(f"%{term}%"))
    )

    return list(session.scalars(statement).all())