from abc import abstractmethod
from typing import Protocol


class PlywayRepo(Protocol):
    @abstractmethod
    def flyway_table_exists(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def create_flyway_table(self) -> bool:
        raise NotImplementedError
