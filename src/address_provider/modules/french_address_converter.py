import re

from address_provider.modules.abstract_class import MyConverter
from address_provider.models import MyData


class FrenchAddressConverter(MyConverter):
    def convert(self, address: str) -> MyData:
        number, street = address.split(',')
        sample_output = {"street": street.strip(), "housenumber": number.strip()}
        return MyData(**sample_output)


if __name__ == '__main__':
    wac = FrenchAddressConverter()
    print(wac.convert("4, rue de la revolution"))
