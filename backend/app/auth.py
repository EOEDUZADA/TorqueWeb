from pwdlib import PasswordHash

from app.models import Employee


password_hash = PasswordHash.recommended()


def register_employee(
    name: str,
    email: str,
    password: str,
) -> Employee:
    return Employee(
        name=name,
        email=email,
        password_hash=password_hash.hash(password),
        active=True,
    )

def login_employee(
    employee: Employee,
    password: str,
) -> Employee | None:

    if not password_hash.verify(password, employee.password_hash):
        return None

    return employee

def get_authenticated_employee(employee: Employee) -> Employee:
    return employee