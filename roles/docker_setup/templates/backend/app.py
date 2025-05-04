from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow React frontend to access API

# PostgreSQL configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@postgres:5432/medicare'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Patient model
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    condition = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'condition': self.condition
        }

# Initialize database
with app.app_context():
    db.create_all()

# API endpoints
@app.route('/patients', methods=['GET'])
def get_patients():
    patients = Patient.query.all()
    return jsonify([patient.to_dict() for patient in patients])

@app.route('/patients', methods=['POST'])
def add_patient():
    data = request.get_json()
    patient = Patient(name=data['name'], age=data['age'], condition=data['condition'])
    db.session.add(patient)
    db.session.commit()
    return jsonify(patient.to_dict()), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)