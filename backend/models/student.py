from extensions import db


class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False,
        unique=True
    )

    full_name = db.Column(
        db.String(150),
        nullable=False
    )

    roll_number = db.Column(
        db.String(20),
        unique=True,
        nullable=False
    )

    branch = db.Column(
        db.String(50),
        nullable=False
    )

    year = db.Column(
        db.Integer,
        nullable=False
    )

    cgpa = db.Column(
        db.Float,
        nullable=False
    )

    skills = db.Column(
        db.Text
    )

    resume = db.Column(
        db.String(255)
    )

    phone = db.Column(
        db.String(15)
    )

    is_placed = db.Column(
        db.Boolean,
        default=False
    )

    user = db.relationship(
        "User",
        back_populates="student"
    )

    applications = db.relationship(
        "Application",
        back_populates="student",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Student {self.full_name}>"