from abc import ABC, abstractmethod
from typing import Any


class AbsService(ABC):
    @abstractmethod
    async def create(self, model: Any, session: Any):
        pass

    @abstractmethod
    async def update(self, pk: int, model: Any, session: Any):
        pass