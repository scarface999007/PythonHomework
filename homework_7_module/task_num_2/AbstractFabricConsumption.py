from abc import ABC, abstractmethod


class AbstractFabricConsumption(ABC):

    @abstractmethod
    def fabric_consumption(self):
        pass
