from flask import Flask
from config import Config
from flask_mail import Mail
import os

mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize config
    config_class.init_app(app)
    
    # Initialize Flask-Mail only if email config is available
    if app.config.get('MAIL_USERNAME') and app.config.get('MAIL_PASSWORD'):
        mail.init_app(app)
    else:
        print("Email configuration not found. Email functionality will be disabled.")

    # Register blueprints
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app 