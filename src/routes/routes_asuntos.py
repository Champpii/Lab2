from flask import Blueprint, request, jsonify
from sqlalchemy.orm import sessionmaker
from conection.db_connection import DBConnection
from models.models_oracle import Asuntos as OracleAsuntos
from models.models_sqlserver import Asuntos as SQLServerAsuntos

asuntos_bp = Blueprint('asuntos', __name__)

db_conn = DBConnection()
oracle_session = sessionmaker(bind=db_conn.get_oracle_engine())()
sqlserver_session_mexico = sessionmaker(bind=db_conn.get_sqlserver_engine_mexico())()
sqlserver_session_el_salvador = sessionmaker(bind=db_conn.get_sqlserver_engine_el_salvador())()

@asuntos_bp.route('/asuntos', methods=['POST'])
def create_asunto():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos faltantes"}), 400

    nuevo_asunto = OracleAsuntos(**data)
    try:
        oracle_session.add(nuevo_asunto)
        oracle_session.commit()

        for session in [sqlserver_session_mexico, sqlserver_session_el_salvador]:
            session.add(SQLServerAsuntos(**data))
            session.commit()

        return jsonify({"message": "Asunto registrado y replicado correctamente"}), 201
    except Exception as e:
        oracle_session.rollback()
        return jsonify({"error": f"Error al crear asunto: {str(e)}"}), 500

@asuntos_bp.route('/asuntos/<int:expediente_id>', methods=['GET'])
def get_asunto(expediente_id):
    asunto = oracle_session.query(OracleAsuntos).filter_by(NumeroExpediente=expediente_id).first()
    if not asunto:
        return jsonify({"error": "Asunto no encontrado"}), 404

    return jsonify(asunto.__dict__), 200
