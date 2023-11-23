from flask import Flask
from routes.region_routes import region_bp
from routes.tax_param_route import car_2_bp
from routes.tax_route import car_bp
from dbase import db


app = Flask(__name__)
app.config['SECRET_KEY'] = '8-800-535-35-35'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/LR5'
app.config['SQLAlchemy_TRACK_MODIFIVATTION'] = False
db.init_app(app)
app.register_blueprint(region_bp)
app.register_blueprint(car_2_bp)
app.register_blueprint(car_bp)
if __name__ == "__main__":
    app.run(debug=True)
