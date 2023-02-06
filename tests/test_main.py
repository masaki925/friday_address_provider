import address_provider.main


def test_main():
    assert address_provider.main.run("Winterallee 3") == {
        "street": "Winterallee", "housenumber": "3"
    }
