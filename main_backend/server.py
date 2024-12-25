from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import face_recognition
import mysql.connector
import numpy as np
import base64

app = Flask(__name__)
CORS(app)

def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="aarati123",  
            database="voting_system"
        )
        return connection
    except mysql.connector.Error as e:
        print(f"Database connection failed: {e}")
        return None

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    frame_data = data['frame']
    voter_id = data['voter_id']
    
    # Decode the frame data
    imgdata = base64.b64decode(frame_data.split(',')[1])
    nparr = np.frombuffer(imgdata, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Process face registration
    face_locations = face_recognition.face_locations(img)
    if len(face_locations) != 1:
        return jsonify({"message": "Please ensure only one face is visible for registration."})

    face_encoding = face_recognition.face_encodings(img, face_locations)[0]
    face_encoding_bytes = face_encoding.tobytes()

    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM voters WHERE voter_id = %s", (voter_id,))
        result = cursor.fetchone()
        if result:
            cursor.close()
            connection.close()
            return jsonify({"message": "Voter ID is already registered."})

        cursor.execute("INSERT INTO voters (voter_id, face_encoding) VALUES (%s, %s)", (voter_id, face_encoding_bytes))
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Registration successful"})
    else:
        return jsonify({"message": "Database connection failed"})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    frame_data = data['frame']
    voter_id = data['voter_id']
    
    # Decode the frame data
    imgdata = base64.b64decode(frame_data.split(',')[1])
    nparr = np.frombuffer(imgdata, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Process face login
    face_locations = face_recognition.face_locations(img)
    if len(face_locations) != 1:
        return jsonify({"message": "Please ensure only one face is visible for login."})

    login_face_encoding = face_recognition.face_encodings(img, face_locations)[0]

    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT face_encoding FROM voters WHERE voter_id = %s", (voter_id,))
        result = cursor.fetchone()
        if result:
            db_face_encoding = np.frombuffer(result[0], dtype=np.float64)
            matches = face_recognition.compare_faces([db_face_encoding], login_face_encoding)
            if matches[0]:
                cursor.close()
                connection.close()
                return jsonify({"message": "Login successful"})
            else:
                cursor.close()
                connection.close()
                return jsonify({"message": "Face did not match. Login failed."})
        else:
            cursor.close()
            connection.close()
            return jsonify({"message": "Voter ID not found in the database."})
    else:
        return jsonify({"message": "Database connection failed"})

if __name__ == '__main__':
    app.run(debug=True)
