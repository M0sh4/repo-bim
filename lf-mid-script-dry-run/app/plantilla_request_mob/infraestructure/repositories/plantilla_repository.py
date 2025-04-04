from app.infraestructure.adapters.db_adapter import DBAdapterSQLAlchemy

class PlantillaRepository:
    def __init__(self):
        self.database_adapter = DBAdapterSQLAlchemy()

    def select_plantilla_mobiquity(self):
        try:
            print(repr("Consultando plantilla request de Comviva. \n plantilla_repository/select_plantilla_mobiquity"))
            nodes = self.database_adapter.select_query()
            if(not nodes or nodes is None or len(nodes)== 0):
                raise ValueError("Error DR: No existe registros de plantillas Mobiquity \n plantilla_repository/select_plantilla_mobiquity")
            return nodes
        except ValueError as ve:
            print(repr(f"Error DR: de valor select_plantilla_mobiquity: {ve} \n plantilla_repository/select_plantilla_mobiquity"))
        except Exception as e:
            print(repr(f"Error DR: general no esperado select_plantilla_mobiquity: {e} \n plantilla_repository/select_plantilla_mobiquity"))