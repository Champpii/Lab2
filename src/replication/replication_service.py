from conection.db_connection import DBConnection
from sqlalchemy.orm import sessionmaker

class ReplicationService:
    def __init__(self):
        self.db_conn = DBConnection()
        self.oracle_engine = self.db_conn.get_oracle_engine()
        self.sqlserver_engine_mexico = self.db_conn.get_sqlserver_engine_mexico()
        self.sqlserver_engine_el_salvador = self.db_conn.get_sqlserver_engine_el_salvador()

    def replicate_clientes(self):
        oracle_session = sessionmaker(bind=self.oracle_engine)()
        sqlserver_session_mexico = sessionmaker(bind=self.sqlserver_engine_mexico)()
        sqlserver_session_el_salvador = sessionmaker(bind=self.sqlserver_engine_el_salvador)()

        clientes = oracle_session.execute("SELECT ClienteID, Nombre, Apellido FROM Clientes").fetchall()

        for cliente in clientes:
            sqlserver_session_mexico.execute(
                "INSERT INTO Clientes (ClienteID, Nombre, Apellido) VALUES (:1, :2, :3)",
                (cliente.ClienteID, cliente.Nombre, cliente.Apellido)
            )
            sqlserver_session_el_salvador.execute(
                "INSERT INTO Clientes (ClienteID, Nombre, Apellido) VALUES (:1, :2, :3)",
                (cliente.ClienteID, cliente.Nombre, cliente.Apellido)
            )

        sqlserver_session_mexico.commit()
        sqlserver_session_el_salvador.commit()

        oracle_session.close()
        sqlserver_session_mexico.close()
        sqlserver_session_el_salvador.close()

        print("Replicación de clientes completada.")

    # Aquí podrías agregar más funciones de replicación para otros modelos
