from abc import ABC, abstractmethod
from typing import Any


class AbsRepository(ABC):
    @abstractmethod
    async def get(self, pk: int, session: Any):
        pass

    @abstractmethod
    async def create(self, model: Any, session: Any):
        pass

    @abstractmethod
    async def delete(self, pk: int, session: Any):
        pass

    @abstractmethod
    async def update(self, pk: int, model, session: Any):
        pass