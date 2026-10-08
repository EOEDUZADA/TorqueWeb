from app.clients import register_client


def test_register_client():
    client = register_client(
        name="João da Silva",
        phone="53999999999",
    )

    assert client.name == "João da Silva"
    assert client.phone == "53999999999"