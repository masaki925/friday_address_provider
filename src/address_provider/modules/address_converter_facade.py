import re

from address_provider.models import MyData

from address_provider.modules.western_address_converter import WesternAddressConverter
from address_provider.modules.german_address_converter import GermanAddressConverter


class AddressConverterFacade():
    def __init__(self, address):
        self.address = address

    def convert(self) -> MyData:
        converter = self.__pickup_converter()
        return converter.convert(self.address)

    def __pickup_converter(self):

        if re.search('ä', self.address):
            converter = GermanAddressConverter()
        else:
            converter = WesternAddressConverter()
        return converter
