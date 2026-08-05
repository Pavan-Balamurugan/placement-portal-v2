from extensions import db
from constants import COMPANY_PENDING


class Company(db.Model):
    __tablename__ = "companies"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False,
        unique=True
    )

    company_name = db.Column(
        db.String(150),
        nullable=False
    )

    industry = db.Column(
        db.String(100),
        nullable=False
    )

    location = db.Column(
        db.String(150),
        nullable=False
    )

    website = db.Column(
        db.String(255)
    )

    hr_name = db.Column(
        db.String(100)
    )

    hr_email = db.Column(
        db.String(120)
    )

    hr_phone = db.Column(
        db.String(15)
    )

    approval_status = db.Column(
        db.String(20),
        default=COMPANY_PENDING
    )

    is_blacklisted = db.Column(
        db.Boolean,
        default=False
    )

    user = db.relationship(
        "User",
        back_populates="company"
    )

    placement_drives = db.relationship(
        "PlacementDrive",
        back_populates="company",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Company {self.company_name}>"