from app import create_app, db

app = create_app('production')

if __name__ == "__main__":
    app.run()
    
# alembic==1.7.7
# click==8.1.3
# dominate==2.6.0
# Flask==2.1.2
# Flask-Bootstrap==3.3.7.1
# Flask-Migrate==3.1.0
# Flask-SQLAlchemy==2.5.1
# Flask-WTF==1.0.1
# greenlet==1.1.2
# importlib-metadata==4.11.3
# importlib-resources==5.7.1
# itsdangerous==2.1.2
# Jinja2==3.1.2
# Mako==1.2.0
# MarkupSafe==2.1.1
# SQLAlchemy==1.4.36
# visitor==0.1.3
# Werkzeug==2.1.2
# WTForms==3.0.1
# zipp==3.8.0