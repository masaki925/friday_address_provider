from address_provider.models import MyData

from .western_address_converter import WesternAddressConverter


class AddressConverterFacade:
    def convert(self, address: str) -> MyData:
        converter = self.__pickup_converter()
        return converter.convert(address)

    def __pickup_converter(self):
        converter = WesternAddressConverter()
        return converter
