# Sailesh Portfolio - Flask Web App

A personal portfolio website built with Flask, featuring information about Sailesh Sivan's work experience, projects, skills, and certifications.

## Features

- Personal portfolio with multiple sections
- Contact form with email functionality
- Resume download/view functionality
- Responsive design with Bootstrap
- Professional styling with custom CSS

## Local Development

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables (create a `.env` file):
   ```
   SECRET_KEY=your-secret-key
   EMAIL_USER=your-email@gmail.com
   EMAIL_PASS=your-app-password
   ```
5. Run the application:
   ```bash
   python run.py
   ```

## Vercel Deployment

This Flask app is configured for deployment on Vercel. The following files are essential for Vercel deployment:

- `vercel.json` - Vercel configuration
- `api/index.py` - API entry point for Vercel
- `runtime.txt` - Python version specification
- `requirements.txt` - Python dependencies

### Deployment Steps

1. Install Vercel CLI:
   ```bash
   npm i -g vercel
   ```

2. Login to Vercel:
   ```bash
   vercel login
   ```

3. Deploy to Vercel:
   ```bash
   vercel
   ```

4. For production deployment:
   ```bash
   vercel --prod
   ```

### Environment Variables

Set the following environment variables in your Vercel dashboard:

- `SECRET_KEY` - Flask secret key
- `EMAIL_USER` - Gmail address for contact form
- `EMAIL_PASS` - Gmail app password
- `MAIL_SERVER` - SMTP server (default: smtp.gmail.com)
- `MAIL_PORT` - SMTP port (default: 587)
- `MAIL_USE_TLS` - Use TLS (default: True)

### Testing Deployment

After deployment, you can test if the app is working by visiting:
- Your main domain (e.g., `https://your-app.vercel.app`)
- Test endpoint: `https://your-app.vercel.app/api/test`

## Project Structure

```
├── api/
│   └── index.py          # Vercel API entry point
├── app/
│   ├── main/
│   │   ├── routes.py     # Flask routes
│   │   └── __init__.py   # Blueprint initialization
│   ├── static/           # Static files (CSS, JS, images)
│   ├── templates/        # HTML templates
│   └── __init__.py       # Flask app factory
├── config.py             # Configuration settings
├── requirements.txt      # Python dependencies
├── runtime.txt           # Python version
├── vercel.json           # Vercel configuration
└── run.py               # Local development entry point
```

## Troubleshooting

### 404 Error on Vercel

If you're getting a 404 error, check:

1. Ensure `vercel.json` is in the root directory
2. Verify `api/index.py` exists and is properly configured
3. Check that all dependencies are in `requirements.txt`
4. Ensure environment variables are set in Vercel dashboard

### Email Functionality

For the contact form to work:

1. Enable 2-factor authentication on your Gmail account
2. Generate an app password
3. Set `EMAIL_USER` and `EMAIL_PASS` environment variables in Vercel

### Static Files

Static files are served from `app/static/` and should be accessible via the `/static/` route.

## License

This project is for personal use and portfolio purposes.
