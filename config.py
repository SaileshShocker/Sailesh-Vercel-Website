import os
from dotenv import load_dotenv

# Only load .env file in development
if os.environ.get('FLASK_ENV') != 'production':
    load_dotenv()

class Config:
    # Basic Configuration
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
    
    # Email Configuration
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'True').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    MAIL_DEFAULT_SENDER = os.environ.get('EMAIL_USER')
    
    # Ensure required config is set
    @staticmethod
    def init_app(app):
        # Only check for email configs if we're in production and email is needed
        if os.environ.get('FLASK_ENV') == 'production':
            required_configs = ['MAIL_USERNAME', 'MAIL_PASSWORD']
            missing_configs = [config for config in required_configs if not app.config.get(config)]
            if missing_configs:
                print(f"Warning: Missing email configurations: {', '.join(missing_configs)}")
                print("Email functionality will be disabled.")

class PersonalInfo:
    # Basic Information
    NAME = "SAILESH SIVAN"
    TITLE = "Data Scientist - Data Analyst| Machine Learning | NLP | GenAI | Computer Vision"
    EMAIL = "sailesh.shocker@gmail.com"
    LOCATION = "Kotagiri, The Nilgiris"
    AVAILABLE_CITIES = ["Bangalore", "Coimbatore"]
    RESUME_PATH = "static/files/SaileshResume.pdf"  # Updated to Flask static path
    
    # Social Links
    LINKEDIN = "https://www.linkedin.com/in/sailesh-shocker/"
    GITHUB = "https://github.com/SaileshShocker"
    TWITTER = "https://x.com/sailesh_shocker"
    
    
    # About Me
    BIO = """
            🚀 AI, Data Science & Analytics Professional
Hey there! 👋 I'm a curious and driven AI, Data Science, and Analytics professional with over 2 years of experience transforming raw data into intelligent solutions that drive business growth.

I work across a wide range of technologies — from 📊 Data Analytics and 🤖 Machine Learning to 💬 Natural Language Processing (NLP), 📚 Large Language Models (LLMs), 🎨 Generative AI, and 👁️ Computer Vision. I've built and deployed several detection models and love solving complex problems with AI.

I specialize in end-to-end development, from analyzing and cleaning data to deploying full-stack AI applications in the cloud.

⚙️ Tools & Technologies I Use:

🐍 Python for ML, automation, and scripting

💾 SQL & MongoDB for working with structured and unstructured data

☁️ AWS, Azure, and Google Cloud Platform for scalable AI solutions

💻 Flask & Streamlit for building interactive apps

📊 Power BI for business intelligence and data visualization

⚙️ MS Power Automate for automating workflows

✨ I'm passionate about building smart, scalable systems and discovering innovative ways to unlock value from data and AI.

When I'm not coding or building, I'm usually sipping coffee ☕ while diving into the latest in AI, NLP, and Generative AI.

Let's connect and build something amazing! 💡
"""
    
    # Current Position
    CURRENT_POSITION = "Associate Data Scientist"
    CURRENT_COMPANY = "Kovai.co"
    CURRENT_ROLE_DESCRIPTION = "Working on data analytics, business intelligence, LLM, Gen AI, and automation solutions."
    
    # Education
    EDUCATION = [
        {
            "degree": "Bachelor of Engineering (Computer Science)",
            "institution": "Karpagam Academy of Higher Education",
            "year": "2020",
            # "description": "Brief description"
        }
    ]
    
    # Certifications
    CERTIFICATIONS = [
        {
            "name": "Microsoft Certified: Power BI Data Analyst Associate",
            "issuer": "Microsoft",
            "year": "2024",
            "credential_id": "2899AA0C5C47954B",
            "certification_number": "06F58E-91E1R3",
            "earned_date": "July 7, 2024"
        },
        {
            "name": "IBM Data Science Professional Certificate",
            "issuer": "IBM",
            "year": "2023",
            "credential_id": ""
        },
        {
            "name": "Data Analysis with Python",
            "issuer": "IBM",
            "year": "2023",
            "credential_id": ""
        },
        {
            "name": "Data Visualization with Python",
            "issuer": "IBM",
            "year": "2023",
            "credential_id": ""
        },
        {
            "name": "Databases and SQL for Data Science",
            "issuer": "IBM",
            "year": "2023",
            "credential_id": ""
        },
        {
            "name": "Python for Data Science",
            "issuer": "IBM",
            "year": "2023",
            "credential_id": ""
        },
        {
            "name": "Machine Learning with Python",
            "issuer": "IBM",
            "year": "2023",
            "credential_id": ""
        },
        {
            "name": "Machine Learning",
            "issuer": "Stanford University",
            "year": "2023",
            "credential_id": ""
        }
    ]
    
    # Skills
    TECHNICAL_SKILLS = [
        "Python",
        "SQL",
        "Machine Learning",
        "Natural Language Processing (NLP)",
        "Large Language Models (LLM)",
        "Generative AI",
        "Computer Vision",
        "Web Scraping",
        "Exploratory Data Analysis",
        "Data Visualization",
        "Power BI",
        "Tableau",
        "Excel",
        "Google Cloud Platform",
        "Microsoft Azure",
        "AWS",
        "MongoDB",
        "Power Automate"
    ]
    
    SOFT_SKILLS = [
        "Problem-solving and analytical thinking",
        "Critical thinking and data-driven decision making",
        "Clear and concise communication",
        "Cross-functional collaboration and teamwork",
        "Strong business acumen",
        "Adaptability in fast-paced environments",
        "Curiosity and passion for continuous learning",
        "Effective time management and prioritization",
        "Storytelling and data visualization"
    ]
    
    # Tools & Platforms
    TOOLS = [
        "Python Libraries (Pandas, NumPy, Scikit-learn)",
        "SQL & Databases",
        "Power BI",
        "Tableau",
        "Microsoft Excel",
        "Google Cloud Platform",
        "Microsoft Azure",
        "AWS",
        "MongoDB",
        "Power Automate",
        "Git",
        "Jupyter Notebooks",
        "Visual Studio Code",
        "Docker"
    ]
    
    # Projects
    PROJECTS = [
        {
            "title": "DOCTOR-AI",
            "date": "December 2023",
            "description": "An AI doctor assistant who can assist you with your health-related concerns and medicines.",
            "tools": ["Python", "NLP", "Large Language Models", "GenAI"],
            "impact": "Providing accessible healthcare assistance through AI technology",
            "link": "#"
        },
        {
            "title": "SISI ASSISTANT - CHATBOT",
            "date": "December 2023",
            "description": "SISI is an AI friend who can help you with various tasks such as providing information, answering questions, setting reminders, giving recommendations, and engaging in casual conversations.",
            "tools": ["Python", "NLP", "LLM", "Generative AI"],
            "impact": "Creating an intelligent personal assistant for daily tasks and interactions",
            "link": "#"
        },
        {
            "title": "LANGUAGE TRANSLATOR",
            "date": "July 2023",
            "description": "Personal interpreter who can translate any language to your desired language.",
            "tools": ["Python", "NLP", "Machine Learning", "Translation APIs"],
            "impact": "Breaking language barriers through AI-powered translation",
            "link": "#"
        },
        {
            "title": "CRICKET WORLD CUP 2023 BATTING ANALYSIS",
            "date": "November 2023",
            "description": "Analyzing the batting statistics of players during the World Cup. The analysis covers various aspects, including total runs, centuries, strike rates, and player consistency.",
            "tools": ["Python", "Pandas", "Data Analysis", "Data Visualization"],
            "impact": "Providing comprehensive insights into cricket performance metrics",
            "link": "#"
        },
        {
            "title": "TEXT DETECTION",
            "date": "August-September 2023",
            "description": "Capturing texts in an image with EasyOCR and using Google API to search for the captured text and provide the results.",
            "tools": ["Python", "EasyOCR", "Computer Vision", "Google API"],
            "impact": "Automating text extraction and search from images",
            "link": "#"
        },
        {
            "title": "SMOKING AND CELLPHONE DETECTION",
            "date": "January-February 2023",
            "description": "Detecting smoke and cellphones in traffic.",
            "tools": ["Python", "Computer Vision", "Deep Learning", "Object Detection"],
            "impact": "Enhancing traffic safety through automated detection systems",
            "link": "#"
        },
        {
            "title": "SENTIMENT ANALYSIS",
            "date": "December 2022",
            "description": "Sentiment analysis and content-based filtering using pre-trained models.",
            "tools": ["Python", "NLP", "Machine Learning", "Pre-trained Models"],
            "impact": "Understanding and analyzing sentiment patterns in text data",
            "link": "#"
        },
        {
            "title": "PNEUMONIA PREDICTION",
            "date": "December 2022",
            "description": "Predicting if a person has pneumonia using a chest X-ray image.",
            "tools": ["Python", "Deep Learning", "Computer Vision", "Medical Imaging"],
            "impact": "Assisting medical diagnosis through AI-powered image analysis",
            "link": "#"
        },
        {
            "title": "DIABETES PREDICTION",
            "date": "November-December 2022",
            "description": "Predicting if the person has diabetes or not. And deploying the model to a webpage using Streamlit.",
            "tools": ["Python", "Machine Learning", "Streamlit", "Web Development"],
            "impact": "Creating accessible healthcare diagnostics through web-based ML models",
            "link": "#"
        }
    ]

    # Work Experience
    WORK_EXPERIENCE = [
        {
            "title": "Associate Data Scientist",
            "company": "Kovai.co",
            "duration": "FEBRUARY 2024 - PRESENT",
            "company_url": "https://www.kovai.co/",
            "description": [
                "Working on advanced data analytics, business intelligence, LLM, Gen AI, and automation solutions",
                "Leading AI/ML initiatives and automation projects",
                "Developing end-to-end data AI solutions"
            ]
        },
        {
            "title": "Data Analyst",
            "company": "Kovai.co",
            "duration": "FEBRUARY 2024 - JULY 2024",
            "company_url": "https://www.kovai.co/",
            "description": [
                "Worked on data analytics and business intelligence projects",
                "Developed AI/ML and automation solutions",
                "Contributed to various data-driven projects"
            ]
        },
        {
            "title": "Data Scientist - SDE 1",
            "company": "The Millionvisions",
            "duration": "MARCH 2023 - JUNE 2023",
            "company_url": "https://www.themillionvisions.com/",
            "description": [
                "Worked as a Data Scientist and Software Development Engineer",
                "Developed and desployed computer vision models.",
                "Developed various object detection models.",
                "Integrated NLP with computer detection models."
            ]
        },
        {
            "title": "DATA ASSOCIATE & ANALYST",
            "company": "SALESKEN.AI",
            "duration": "FEBRUARY 2022 - OCTOBER 2022",
            "company_url": "https://www.salesken.ai/",
            "description": [
                "Evaluating Machine Learning Model performance on Production Data.",
                "Creating interactive and dynamic dashboards, stories, and worksheets in Tableau on business datasets, uploading them in Tableau online, and ensuring client data is secure.",
                "Performing Exploratory Data Analysis tasks for the team and delegate tasks to a team member.",
                "Assisting in the testing, developing, and deploying the data science team."
            ]
        }
    ]

    # Internships
    INTERNSHIPS = [
        {
            "title": "Data Analyst",
            "company": "Salesken.ai",
            "duration": "NOVEMBER 2021 - FEBRUARY 2022",
            "company_url": "https://www.salesken.ai/",
            "description": [
                "Evaluating Machine Learning Model Performance on Production Data",
                "Creating interactive and dynamic dashboards, stories, and worksheets in Tableau on business datasets",
                "Uploading dashboards in Tableau online and ensuring client data security"
            ]
        },
        {
            "title": "Data Scientist",
            "company": "iSmile Technologies",
            "duration": "AUGUST 2020 - DECEMBER 2020",
            "company_url": "https://ismiletechnologies.com/en-in/",
            "description": [
                "Building an Email Prioritization model using BigQuery ML with GCP",
                "Integrating IT with Gmail API using Python and WordPress"
            ]
        }
    ] 