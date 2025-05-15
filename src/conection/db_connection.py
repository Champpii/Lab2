from sqlalchemy import create_engine
import os

class DBConnection:
    def __init__(self):
        self.oracle_url = os.environ.get("ORACLE_CONN_STRING")  # Ejemplo: "oracle+cx_oracle://user:pass@host:port/dbname"
        self.sqlserver_url_mexico = os.environ.get("SQLSERVER_CONN_STRING_MEXICO")  # "mssql+pyodbc://user:pass@host/db?driver=ODBC+Driver+17+for+SQL+Server"
        self.sqlserver_url_el_salvador = os.environ.get("SQLSERVER_CONN_STRING_EL_SALVADOR")

    def get_oracle_engine(self):
        return create_engine(self.oracle_url)

    def get_sqlserver_engine_mexico(self):
        return create_engine(self.sqlserver_url_mexico)

    def get_sqlserver_engine_el_salvador(self):
        return create_engine(self.sqlserver_url_el_salvador)
