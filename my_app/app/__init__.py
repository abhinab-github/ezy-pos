from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    # Configure app
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ezy_pos.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'ezypossecret'

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Enable CORS with specific configurations
    CORS(app, supports_credentials=True, resources={r"/*": {"origins": "http://localhost:3000"}})

    # Register Blueprints
    from .routes import auth_routes, inventory_routes, customer_routes, sale_routes, purchase_routes, dashboard_routes
    app.register_blueprint(auth_routes.bp)
    app.register_blueprint(inventory_routes.bp)
    app.register_blueprint(customer_routes.bp)
    app.register_blueprint(sale_routes.bp)
    app.register_blueprint(purchase_routes.bp)
    app.register_blueprint(dashboard_routes.bp)
    # app.register_blueprint(report_routes.bp)
    for rule in app.url_map.iter_rules():
        print(rule)

    # Handle preflight requests (OPTIONS)
    @app.before_request
    def handle_options_request():
        if request.method == 'OPTIONS':
            response = app.make_default_options_response()
            headers = response.headers

            headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
            headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
            headers['Access-Control-Allow-Headers'] = 'Authorization, Content-Type, X-Requested-With'
            headers['Access-Control-Allow-Credentials'] = 'true'

            return response

    # Ensure CORS headers are added to all responses
    @app.after_request
    def add_cors_headers(response):
        response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Authorization, Content-Type, X-Requested-With'
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        return response

    return app
