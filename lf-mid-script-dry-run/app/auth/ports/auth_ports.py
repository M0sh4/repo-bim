from abc import ABC, abstractmethod
from typing import Optional

class AuthPort(ABC):
    @abstractmethod
    def get_token_login(self, type_token_api: str) -> Optional[str]:
        """Obtiene el mapeo entre EWP y Mobiquity."""
        pass