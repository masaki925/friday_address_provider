from abc import ABCMeta, abstractmethod

from address_provider.models import MyData


class MyConverter(metaclass=ABCMeta):
    @abstractmethod
    def convert(address: str) -> MyData:
        pass
