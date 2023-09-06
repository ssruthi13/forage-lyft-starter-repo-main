from abc import ABC, abstractmethod
from serviceable import serviceable

class battery(serviceable):
    @abstractmethod
    def need_service(self) -> bool:
        pass