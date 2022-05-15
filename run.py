from app import create_app, db

app = create_app('production')

if __name__ == "__main__":
    app.run()
    
    
# click==8.1.3
# Flask==2.1.2
# Flask-WTF==1.0.1
# greenlet==1.1.2
# importlib-metadata==4.11.3
# itsdangerous==2.1.2
# Jinja2==3.1.2
# MarkupSafe==2.1.1
# SQLAlchemy==1.4.36
# Werkzeug==2.1.2
# WTForms==3.0.1
# zipp==3.8.0