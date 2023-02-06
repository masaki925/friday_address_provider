from .models import MyData
from .modules.address_converter_facade import AddressConverterFacade


def run(address: str) -> str:
    acf = AddressConverterFacade()
    res = acf.convert(address)
    return res.dict()


if __name__ == "__main__":
    print(run("Winterallee 3"))
