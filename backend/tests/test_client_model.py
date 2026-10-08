from app.models import Client


def test_client_model():
    client = Client(
        name="João da Silva",
        phone="53999999999",
    )

    assert client.name == "João da Silva"
    assert client.phone == "53999999999"
