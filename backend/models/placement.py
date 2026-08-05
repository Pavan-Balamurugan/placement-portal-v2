from extensions import db


class Placement(db.Model):
    __tablename__ = "placements"

    id = db.Column(db.Integer, primary_key=True)

    application_id = db.Column(
        db.Integer,
        db.ForeignKey("applications.id"),
        nullable=False,
        unique=True
    )

    position = db.Column(
        db.String(100),
        nullable=False
    )

    salary = db.Column(
        db.Float,
        nullable=False
    )

    joining_date = db.Column(
        db.Date
    )

    offer_letter = db.Column(
        db.String(255)
    )

    application = db.relationship(
        "Application",
        back_populates="placement"
    )

    def __repr__(self):
        return f"<Placement {self.position}>"