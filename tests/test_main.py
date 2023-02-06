import address_provider.main
import pytest


testdata = [
    ("Winterallee 3", {"street": "Winterallee", "housenumber": "3"}),
    ("Musterstrasse 45", {"street": "Musterstrasse", "housenumber": "45"}),
    ("Blaufeldweg 123B", {"street": "Blaufeldweg", "housenumber": "123B"}),
]

testdata2 = [
    ("Am Bächle 23", {"street": "Am Bächle", "housenumber": "23"}),
    ("Auf der Vogelwiese 23 b", {"street": "Auf der Vogelwiese", "housenumber": "23 b"}),
]


@pytest.mark.parametrize("address, expected", testdata)
def test_main(address, expected):
    assert address_provider.main.run(address) == expected


@pytest.mark.parametrize("address, expected", testdata2)
def test_main2(address, expected):
    assert address_provider.main.run(address) == expected
