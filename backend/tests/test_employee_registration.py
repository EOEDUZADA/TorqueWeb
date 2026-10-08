from app.auth import register_employee


def test_register_employee_hashes_password():
    employee = register_employee(
        name="João",
        email="joao@example.com",
        password="123456",
    )

    assert employee.name == "João"
    assert employee.email == "joao@example.com"
    assert employee.password_hash != "123456"
    assert employee.password_hash
    assert employee.active is True