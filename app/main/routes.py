from flask import render_template, send_file, jsonify, request
from app.main import bp
from config import PersonalInfo
import os
from app import mail
from flask_mail import Message

@bp.route('/')
@bp.route('/home')
def index():
    return render_template('home.html', info=PersonalInfo)

@bp.route('/about')
def about():
    return render_template('about.html', info=PersonalInfo)

@bp.route('/skills')
def skills():
    return render_template('skills.html', info=PersonalInfo)

@bp.route('/projects')
def projects():
    return render_template('projects.html', info=PersonalInfo)

@bp.route('/resume')
def resume():
    return render_template('resume.html', info=PersonalInfo)

@bp.route('/resume/view')
def view_resume():
    app_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    resume_path = os.path.join(app_dir, PersonalInfo.RESUME_PATH)
    try:
        return send_file(resume_path)
    except Exception as e:
        return f"Error: Could not find resume file at {resume_path}", 404

@bp.route('/resume/download')
def download_resume():
    app_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    resume_path = os.path.join(app_dir, PersonalInfo.RESUME_PATH)
    try:
        return send_file(resume_path, as_attachment=True)
    except Exception as e:
        return f"Error: Could not find resume file at {resume_path}", 404

@bp.route('/contact')
def contact():
    return render_template('contact.html', info=PersonalInfo)

@bp.route('/send_message', methods=['POST'])
def send_message():
    try:
        data = request.get_json()
        
        # Create email message
        msg = Message(
            subject=f"Portfolio Contact: {data['subject']}",
            recipients=[PersonalInfo.EMAIL],
            body=f"""
            New message from your portfolio website:
            
            From: {data['name']} <{data['email']}>
            Subject: {data['subject']}
            
            Message:
            {data['message']}
            """)
        
        # Send email
        mail.send(msg)
        
        return jsonify({"status": "success", "message": "Email sent successfully!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@bp.route('/certifications')
def certifications():
    return render_template('certifications.html', info=PersonalInfo) 