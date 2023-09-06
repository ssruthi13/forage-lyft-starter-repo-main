from abc import ABC, abstractmethod
from serviceable import serviceable


class Car(serviceable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    @abstractmethod
    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()