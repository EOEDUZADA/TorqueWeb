from app.auth import login_employee, password_hash
from app.models import Employee


def test_login_with_correct_password():
    employee = Employee(
        name="João",
        email="joao@example.com",
        password_hash=password_hash.hash("123456"),
        active=True,
    )

    authenticated_employee = login_employee(
        employee,
        "123456", #Senha utilizada para testar o login
    )

    assert authenticated_employee == employee


def test_login_with_wrong_password():
    employee = Employee(
        name="João",
        email="joao@example.com",
        password_hash=password_hash.hash("123456"),
        active=True,
    )

    authenticated_employee = login_employee(
        employee,
        "senha-errada", #Senha utilizada para testar o login
    )

    assert authenticated_employee is None