from address_provider.main import AddressConverter, MyData


def test_main():
    ac = AddressConverter()
    assert ac.run("Winterallee 3") == MyData(
        **{"street": "Winterallee", "housenumber": "3"}
    )
