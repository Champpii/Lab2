from flask import Blueprint, request, jsonify
from sqlalchemy.orm import sessionmaker
from conection.db_connection import DBConnection
from models.models_oracle import Gabinetes as OracleGabinetes
from models.models_sqlserver import Gabinetes as SQLServerGabinetes

gabinetes_bp = Blueprint('gabinetes', __name__)

db_conn = DBConnection()
oracle_session = sessionmaker(bind=db_conn.get_oracle_engine())()
sqlserver_session_mexico = sessionmaker(bind=db_conn.get_sqlserver_engine_mexico())()
sqlserver_session_el_salvador = sessionmaker(bind=db_conn.get_sqlserver_engine_el_salvador())()

@gabinetes_bp.route('/gabinetes', methods=['POST'])
def create_gabinete():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos faltantes"}), 400

    nuevo_gabinete = OracleGabinetes(**data)
    try:
        oracle_session.add(nuevo_gabinete)
        oracle_session.commit()

        for session in [sqlserver_session_mexico, sqlserver_session_el_salvador]:
            session.add(SQLServerGabinetes(**data))
            session.commit()

        return jsonify({"message": "Gabinete registrado y replicado correctamente"}), 201
    except Exception as e:
        oracle_session.rollback()
        return jsonify({"error": f"Error al crear gabinete: {str(e)}"}), 500
