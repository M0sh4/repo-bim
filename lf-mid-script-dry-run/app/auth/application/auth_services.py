"""s
"""
from app.auth.ports.auth_ports import AuthPort
from app.auth.infraestructure.repositories.auth_repository import AuthRepository

class AuthService(AuthPort):

    def __init__(self,ambiente, conexion, table_proceso):
        self.ambiente = ambiente
        self.conexion = conexion
        self.table_proceso = table_proceso
        self.auth_repository = AuthRepository(self.ambiente, self.conexion, self.table_proceso)


    def get_token_login(self, type_token_api, item_id, contexto_encontrado,msisdn_token):
        token = self.auth_repository.get_token(type_token_api, item_id,contexto_encontrado,msisdn_token)
        
        return token
