from flask import Flask
from routes.routes_clientes import clientes_bp
from routes.routes_asuntos import asuntos_bp
from routes.routes_gabinete import gabinetes_bp

app = Flask(__name__)

# Registrar los endpoints con Flask
app.register_blueprint(clientes_bp, url_prefix="/api")
app.register_blueprint(asuntos_bp, url_prefix="/api")
app.register_blueprint(gabinetes_bp, url_prefix="/api")

@app.route('/ping', methods=['GET'])
def ping():
    """Endpoint simple para probar la disponibilidad del servicio."""
    return {"status": "alive"}, 200

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
