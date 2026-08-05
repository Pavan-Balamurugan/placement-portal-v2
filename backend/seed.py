from werkzeug.security import generate_password_hash

from app import app
from extensions import db
from models import User
from constants import ROLE_ADMIN


with app.app_context():

    admin = User.query.filter_by(
        role=ROLE_ADMIN
    ).first()

    if admin is None:

        admin = User(
            email="admin@placement.com",
            password=generate_password_hash("admin123"),
            role=ROLE_ADMIN
        )

        db.session.add(admin)
        db.session.commit()

        print("Admin created successfully.")

    else:
        print("Admin already exists.")