from pydantic import BaseModel


class MyData(BaseModel):
    street: str
    housenumber: str


class AddressConverter:
    def run(self, address: str) -> MyData:
        sample_data = {"street": "Winterallee", "housenumber": "3"}
        return MyData(**sample_data)


if __name__ == "__main__":
    ac = AddressConverter()
    res = ac.run("Winterallee 3")
    print(res)
