from app.models import Vehicle


def test_vehicle_model():
    vehicle = Vehicle(
        plate="ABC1D23",
        brand="Volkswagen",
        model="Gol",
        year=2020,
        mileage=50000,
    )

    assert vehicle.plate == "ABC1D23"
    assert vehicle.brand == "Volkswagen"
    assert vehicle.model == "Gol"
    assert vehicle.year == 2020
    assert vehicle.mileage == 50000