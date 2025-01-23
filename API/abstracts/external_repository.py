from abc import ABC, abstractmethod
from typing import Any


class AbsDataFetcher(ABC):
    @abstractmethod
    async def fetch_data(self, pk: int, session: Any):
        pass
