import re

from address_provider.modules.abstract_class import MyConverter
from address_provider.models import MyData


class GermanAddressConverter(MyConverter):
    def convert(self, address: str) -> MyData:
        number_start_at = re.search(r'\d+', address).start()
        street = address[:number_start_at].strip()
        number = address[number_start_at:].strip()
        sample_output = {"street": street, "housenumber": number}
        return MyData(**sample_output)


if __name__ == '__main__':
    wac = GermanAddressConverter()
    print(wac.convert("Am Bächle 23"))
