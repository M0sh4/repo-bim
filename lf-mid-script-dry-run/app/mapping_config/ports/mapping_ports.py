from abc import ABC, abstractmethod
from typing import Tuple, Optional

class MappingPort(ABC):
    @abstractmethod
    def get_mapping_ewp_comviva(self, start_date: str, end_date: str, format_fecha: str) -> Optional[Tuple[str, str, str]]:
        """Obtiene el mapeo entre EWP y Mobiquity."""
        pass
