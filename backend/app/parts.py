
from decimal import Decimal

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Part


def register_part(
    name: str,
    code: str,
    category: str,
    price: Decimal,
    quantity_available: int,
) -> Part:
    return Part(
        name=name,
        code=code,
        category=category,
        price=price,
        quantity_available=quantity_available,
        active=True,
    )


def search_parts(
    session: Session,
    term: str,
) -> list[Part]:
    statement = select(Part).where(
        Part.name.ilike(f"%{term}%")
        | Part.code.ilike(f"%{term}%")
    )

    return list(session.scalars(statement).all())


#Disponibilidade da peça
def is_part_available(part: Part) -> bool:
    return part.quantity_available > 0



def update_part_stock(part: Part, quantity: int) -> None:
    if quantity < 0:
        raise ValueError("A quantidade não pode ser negativa")

    part.quantity_available = quantity