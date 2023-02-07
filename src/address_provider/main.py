import argparse

from address_provider.modules.address_converter_facade import AddressConverterFacade


def run(address: str) -> str:
    acf = AddressConverterFacade(address)
    res = acf.convert()
    return res.dict()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--address", type=str, required=True)
    args = parser.parse_args()

    print(run(args.address))
