from app.models import Employee


def test_employee_model():
    employee = Employee(
        name="João",
        email="joao@example.com",
        password_hash="hashed-password",
        active = True
    )

    assert employee.name == "João"
    assert employee.email == "joao@example.com"
    assert employee.password_hash == "hashed-password"
    assert employee.active is True