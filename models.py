from dbase import db
from sqlalchemy.orm import relationship

class Region(db.Model):
    __tablename__ = 'region'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    car_tax_params = relationship(
        'CarTaxParam',
        backref='region',
        cascade='save-update, merge, delete'
    )


class CarTaxParam(db.Model):
    __tablename__ = 'car_tax_param'

    id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey('region.id'), nullable=False)
    from_hp_car = db.Column(db.Integer, nullable=False)
    to_hp_car = db.Column(db.Integer, nullable=False)
    from_production_year_car = db.Column(db.Integer, nullable=False)
    to_production_year_car = db.Column(db.Integer, nullable=False)
    rate = db.Column(db.Numeric, nullable=False)

    regions = relationship(
        'Region',
        backref='car_tax_param',
        cascade='save-update, merge, delete'
    )
