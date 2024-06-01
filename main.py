from flask import Flask, request, jsonify, make_response, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_cors import CORS
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/FashionAI- RS/users.db'
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
CORS(app)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Database model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return 'Welcome to the Flask app!'

@app.route('/test', methods=['GET'])
def test():
    return jsonify('test ok')

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if not name or not email or not password:
        return jsonify({"error": "Name, email, and password are required"}), 400
    
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({"error": "Email already registered"}), 409

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    
    new_user = User(name=name, email=email, password=hashed_password)
    
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({
            "message": "User registered successfully",
            "user": {
                "name": new_user.name,
                "email": new_user.email,
                "id": new_user.id
            }
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 422

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400
    
    user = User.query.filter_by(email=email).first()
    
    if user and bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity={'email': user.email, 'id': user.id})
        user_data = {
            'id': user.id,
            'name': user.name,
            'email': user.email
        }
        response = make_response(jsonify(user=user_data))
        response.set_cookie('token', access_token)
        return response
    else:
        return jsonify({"error": "Invalid email or password"}), 401

@app.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    current_user = get_jwt_identity()
    user = User.query.get(current_user.get('id'))
    
    if user:
        return jsonify({
            'name': user.name,
            'email': user.email,
            'id': user.id
        })
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/logout', methods=['POST'])
def logout():
    response = make_response(jsonify(True))
    response.set_cookie('token', '', expires=0)
    return response

@app.route('/images', methods=['GET'])
def get_images():
    images = [
        '0110065001.jpg', '0110065002.jpg', '0110065011.jpg', '0111593001.jpg', '0118458003.jpg',
        '0110065001.jpg', '0110065002.jpg', '0110065011.jpg', '0111593001.jpg', '0118458003.jpg',
        '0110065001.jpg', '0110065002.jpg', '0110065011.jpg', '0111593001.jpg', '0118458003.jpg',
        '0110065001.jpg', '0110065002.jpg', '0110065011.jpg', '0111593001.jpg', '0118458003.jpg'
    ]
    return jsonify(images)

@app.route('/selected-images', methods=['POST'])
def selected_images():
    data = request.json
    selected_images = data.get('selected_images')
    if not selected_images or len(selected_images) < 5:
        return jsonify({"error": "At least 5 images must be selected"}), 400
    
    recommended_images = [f"recommended_{i}.jpg" for i in range(1, 6)]
    return jsonify(recommended_images)

@app.route('/uploads/<filename>')
def serve_image(filename):
    directory = 'C:/FashionAI- RS/images/011'
    return send_from_directory(directory, filename)

if __name__ == '__main__':
    app.run(debug=True)