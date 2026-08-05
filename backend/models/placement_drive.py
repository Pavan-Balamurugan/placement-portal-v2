from extensions import db
from constants import DRIVE_PENDING


class PlacementDrive(db.Model):
    __tablename__ = "placement_drives"

    id = db.Column(db.Integer, primary_key=True)

    company_id = db.Column(
        db.Integer,
        db.ForeignKey("companies.id"),
        nullable=False
    )

    job_title = db.Column(
        db.String(150),
        nullable=False
    )

    job_description = db.Column(
        db.Text,
        nullable=False
    )

    required_skills = db.Column(
        db.Text
    )

    salary = db.Column(
        db.Float,
        nullable=False
    )

    location = db.Column(
        db.String(100)
    )

    employment_type = db.Column(
        db.String(50),
        default="Full Time"
    )

    experience_required = db.Column(
        db.String(50),
        default="Fresher"
    )

    eligibility_branch = db.Column(
        db.String(255)
    )

    minimum_cgpa = db.Column(
        db.Float,
        default=0.0
    )

    application_deadline = db.Column(
        db.Date
    )

    status = db.Column(
        db.String(20),
        default=DRIVE_PENDING
    )

    company = db.relationship(
        "Company",
        back_populates="placement_drives"
    )

    applications = db.relationship(
        "Application",
        back_populates="placement_drive",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<PlacementDrive {self.job_title}>"