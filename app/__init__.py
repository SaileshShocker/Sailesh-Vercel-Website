from flask import Flask
from config import Config
from flask_mail import Mail

mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize config
    config_class.init_app(app)
    
    # Initialize Flask-Mail
    mail.init_app(app)

    # Register blueprints
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app 