from datetime import datetime

from extensions import db
from constants import APPLICATION_APPLIED


class Application(db.Model):
    __tablename__ = "applications"

    id = db.Column(db.Integer, primary_key=True)

    student_id = db.Column(
        db.Integer,
        db.ForeignKey("students.id"),
        nullable=False
    )

    placement_drive_id = db.Column(
        db.Integer,
        db.ForeignKey("placement_drives.id"),
        nullable=False
    )

    application_date = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    status = db.Column(
        db.String(20),
        default=APPLICATION_APPLIED
    )

    feedback = db.Column(
        db.Text
    )

    interview_date = db.Column(
        db.DateTime
    )

    student = db.relationship(
        "Student",
        back_populates="applications"
    )

    placement_drive = db.relationship(
        "PlacementDrive",
        back_populates="applications"
    )

    placement = db.relationship(
        "Placement",
        back_populates="application",
        uselist=False,
        cascade="all, delete-orphan"
    )

    __table_args__ = (
        db.UniqueConstraint(
            "student_id",
            "placement_drive_id",
            name="unique_student_application"
        ),
    )

    def __repr__(self):
        return f"<Application {self.id}>"