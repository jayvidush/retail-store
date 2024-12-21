from app.routes.test_routes import bp

def register_routes(app):
    app.register_blueprint(bp)