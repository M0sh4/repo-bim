from abc import ABC, abstractmethod

class PlantillaPort(ABC):
    
    @abstractmethod
    def get_plantilla_json_mobiquity(self):
        """Método abstracto que debe implementarse para obtener plantillas de Mobiquity."""
        pass