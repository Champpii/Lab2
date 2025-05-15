import os

class FlaskConfig:
    """Clase de configuración para Flask."""
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "ClaveSecretaSegura")  # Se recomienda cambiar esto en producción
    DEBUG = True  # Cambiar a False en producción
    
    # Configuración de bases de datos
    ORACLE_CONN_STRING = os.environ.get("ORACLE_CONN_STRING")
    SQLSERVER_CONN_STRING_MEXICO = os.environ.get("SQLSERVER_CONN_STRING_MEXICO")
    SQLSERVER_CONN_STRING_EL_SALVADOR = os.environ.get("SQLSERVER_CONN_STRING_EL_SALVADOR")
    
    @classmethod
    def get_database_uri(cls, db_type):
        """Retorna la URI de conexión según el tipo de base de datos."""
        if db_type == "oracle":
            return cls.ORACLE_CONN_STRING
        elif db_type == "sqlserver_mexico":
            return cls.SQLSERVER_CONN_STRING_MEXICO
        elif db_type == "sqlserver_el_salvador":
            return cls.SQLSERVER_CONN_STRING_EL_SALVADOR
        else:
            raise ValueError("Base de datos no soportada.")
