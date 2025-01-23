from abc import ABC, abstractmethod
from typing import Any


class AbsDataFetcher(ABC):
    @abstractmethod
    async def fetch_data(self, session: Any, pk: int):
        pass
