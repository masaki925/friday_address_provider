from address_provider.models import MyData


class WesternAddressConverter():
    def convert(self, address: str) -> MyData:
        street, number = address.split()
        sample_output = {"street": street, "housenumber": number}
        return MyData(**sample_output)


if __name__ == '__main__':
    wac = WesternAddressConverter()
    wac.convert("something 3")
