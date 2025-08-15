from app import create_app
from datetime import datetime

app = create_app()

@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

# Add a simple test endpoint
@app.route('/api/test')
def test():
    return {'message': 'Flask app is working on Vercel!'}

# This is the entry point for Vercel
app.debug = False
