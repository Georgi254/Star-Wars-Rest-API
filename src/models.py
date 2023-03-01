from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorite_planet = db.relatioship('Planets', secondary=user_planet)
    favorite_character = db.relatioship('Characters', secondary=user_character)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=true)
    name = db.Column(sb.String(100))
    gender = db.Column(db.String(30))
    height = db.Column(db.Integer)

    def __repr__(self):
        return '<Characters %r>' % self.id

    def serialize(self):
        return {'id':self.id,
                'name':self.name,
                'gender':self.gender,
                'height':self.height}

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    population = db.Column(db.String(250))
    terrain = db.Column(db.String(250))
    climate = db.Column(db.String(100))
    orbital_period = db.Column(db.String(100))
    rotation_period = db.Column(db.String(100))
    diameter = db.Column(db.String(100))

    def __repr__(self):
        return '<Planets %r>' % self.id

    def serialize(self):
        return {"id": self.id,
                "name": self.name,
                "population": self.population,
                "terrain": self.terrain,
                "climate": self.climate,
                "orbital_period": self.orbital_period,
                "rotation_period": self.rotation_period,
                "diameter": self.diameter}

class Starships(db.models):
    id = db.Column(db.Integer, primary_key=True)
    manufactured = db.Column(db.String(250))
    model = db.Column(db.String(250))
    cost_in_credits = db.Column(db.Integer)
    length = db.Column(db.Integer)
    passengers = db.Column(db.Integer)

    def __repr__(self):
        return '<Starships %r>' % self.id

    def serialize(self):
        return {'id':self.id,
                'manufactured':self.manufactured,
                'model':self.model,
                'cost_in_credits':self.cost_in_credits,
                'length':self.length,
                'passengers':self.passengers}
