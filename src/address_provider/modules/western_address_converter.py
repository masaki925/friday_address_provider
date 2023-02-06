from address_provider.models import MyData


class WesternAddressConverter():
    def convert(self, address_string: str) -> MyData:
        # address_string = "Winterallee 3"
        sample_output = {"street": "Winterallee", "housenumber": "3"}
        return MyData(**sample_output)
