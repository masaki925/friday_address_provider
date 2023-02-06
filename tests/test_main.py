import address_provider.main
import pytest


testdata = [
    ("Winterallee 3", {"street": "Winterallee", "housenumber": "3"}),
    ("Musterstrasse 45", {"street": "Musterstrasse", "housenumber": "45"}),
    ("Blaufeldweg 123B", {"street": "Blaufeldweg", "housenumber": "123B"}),
]


@pytest.mark.parametrize("address, expected", testdata)
def test_main(address, expected):
    assert address_provider.main.run(address) == expected
