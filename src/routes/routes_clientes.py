from flask import Blueprint, request, jsonify
from sqlalchemy.orm import sessionmaker
from conection.db_connection import DBConnection
from models.models_oracle import Clientes as OracleClientes
from models.models_sqlserver import Clientes as SQLServerClientes

clientes_bp = Blueprint('clientes', __name__)

db_conn = DBConnection()
oracle_session = sessionmaker(bind=db_conn.get_oracle_engine())()
sqlserver_session_mexico = sessionmaker(bind=db_conn.get_sqlserver_engine_mexico())()
sqlserver_session_el_salvador = sessionmaker(bind=db_conn.get_sqlserver_engine_el_salvador())()

@clientes_bp.route('/clientes', methods=['POST'])
def create_cliente():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos faltantes"}), 400

    nuevo_cliente = OracleClientes(**data)
    try:
        oracle_session.add(nuevo_cliente)
        oracle_session.commit()

        for session in [sqlserver_session_mexico, sqlserver_session_el_salvador]:
            session.add(SQLServerClientes(**data))
            session.commit()

        return jsonify({"message": "Cliente registrado y replicado correctamente"}), 201
    except Exception as e:
        oracle_session.rollback()
        return jsonify({"error": f"Error al crear cliente: {str(e)}"}), 500

@clientes_bp.route('/clientes/<int:cliente_id>', methods=['GET'])
def get_cliente(cliente_id):
    cliente = oracle_session.query(OracleClientes).filter_by(ClienteID=cliente_id).first()
    if not cliente:
        return jsonify({"error": "Cliente no encontrado"}), 404

    return jsonify(cliente.__dict__), 200
