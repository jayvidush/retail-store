from app.routes.product_routes import product_bp  # Similar setup for other routes

def register_routes(app):
    app.register_blueprint(product_bp)