from starlette.config import Config as StarletteConfig

class Config:
    def __init__(self, env_file=".env"):
        self.config_instance = StarletteConfig(env_file=env_file)

    @staticmethod
    def _str_to_bool(value: str) -> bool:
        if value.lower() in ["true", "1", "yes", "y"]:
            return True
        if value.lower() in ["false", "0", "no", "n"]:
            return False
        raise ValueError(f"Invalid boolean value: {value}")

    def get_environment_variable(self, environment_variable: str, as_bool: bool = False):
        value = self.config_instance(environment_variable)
        if as_bool:
            return self._str_to_bool(value)
        return value
