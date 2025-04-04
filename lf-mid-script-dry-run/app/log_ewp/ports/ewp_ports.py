from abc import ABC, abstractmethod
from typing import Tuple, Optional

class EWPPort(ABC):
    @abstractmethod
    async def get_select_log_asincrona(self,start_date, end_date, limit, flujo_api, id_logs) -> Optional[list]:
        """Obtiene el mapeo entre EWP y Mobiquity."""
        pass
    