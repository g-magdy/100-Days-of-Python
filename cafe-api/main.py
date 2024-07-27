from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random
'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)
    
    def to_dict(self):
        dictionary = {}
        
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        
        return dictionary


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def get_random_cafe():
    result = db.session.execute(db.select(Cafe)).scalars().all()
    random_cafe : Cafe= random.choice(result)
 
    return jsonify(random_cafe.to_dict())

@app.route("/all")
def get_all():
    result = db.session.execute(db.select(Cafe)).scalars().all()
    
    result = [cafe.to_dict() for cafe in result]
    
    return jsonify(result)

@app.route("/search")
def search():
    loc = request.args.get("loc")
    result = db.session.execute(db.select(Cafe).where(Cafe.location == loc)).scalars().all()
    if loc is not None and result != []:
        return jsonify(cafes=[r.to_dict() for r in result])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404
        

# HTTP GET - Read Record

# HTTP POST - Create Record
@app.route("/add", methods = ["POST"])
def add_cafe():
    new_cafe = Cafe()
    new_cafe.name = request.form.get("name")
    new_cafe.map_url = request.form.get("map_url")
    new_cafe.img_url = request.form.get("img_url")
    new_cafe.location = request.form.get("location")
    new_cafe.seats = request.form.get("seats")
    new_cafe.has_toilet = bool(request.form.get("has_toilet"))
    new_cafe.has_wifi = bool(request.form.get("has_wifi"))
    new_cafe.has_sockets = bool(request.form.get("has_sockets"))
    new_cafe.can_take_calls = bool(request.form.get("can_take_calls"))
    new_cafe.coffee_price = request.form.get("coffee_price")
    
    db.session.add(new_cafe)
    
    # ! this  is really important
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})
    

# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_coffee_price(cafe_id):
    target = db.get_or_404(Cafe, cafe_id)
    if target is not None:
        target.coffee_price = f'£{int(request.args.get("new_price"))}'
        db.session.commit()
        return jsonify(response={"success": f"updated cafe with id={cafe_id} to {target.coffee_price}"})
    else:
        return jsonify(response={"fail": "no cafe with the given id"}), 404

# HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def report_closed(cafe_id):
    if "TopSecretAPIKey" == request.args.get("api_key"):
        
        target = db.get_or_404(Cafe, int(cafe_id))
        
        if target is not None:
            db.session.delete(target)
            db.session.commit()
            return jsonify(reqponse={"success": f"cafe {target.name} was deleted successfully"})
        
        return jsonify(reqponse={"fail": "cafe does not exist"}), 404
        
    else:
        return jsonify(reqponse={"fail": "you are not authorized"}), 403
    
    


if __name__ == '__main__':
    app.run(debug=True)
