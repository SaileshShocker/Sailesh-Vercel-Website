from app import create_app
from datetime import datetime
import os
from flask import send_from_directory

# Set environment for Vercel
os.environ['FLASK_ENV'] = 'production'

try:
    app = create_app()
    
    @app.context_processor
    def inject_now():
        return {'now': datetime.utcnow()}

    # Add a simple test endpoint
    @app.route('/api/test')
    def test():
        return {'message': 'Flask app is working on Vercel!'}

    # Custom static file handler for Vercel
    @app.route('/static/<path:filename>')
    def custom_static(filename):
        return send_from_directory('app/static', filename)

    # This is the entry point for Vercel
    app.debug = False
    
except Exception as e:
    print(f"Error initializing Flask app: {e}")
    raise
