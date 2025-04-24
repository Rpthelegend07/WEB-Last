from flask import Flask, request, jsonify
from flask_cors import CORS
from db_config import connect

app = Flask(__name__)
CORS(app, origins=["http://127.0.0.1:5500"])  # ← this allows all origins (localhost, 5500, etc.)  # Allow cross-origin requests for local testing
@app.route("/")
def home():
    return "<h2>Flask backend is running. Try submitting the contact form.</h2>"
@app.route("/submit-form", methods=["POST"])
def submit_form():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    subject = data.get("subject")
    message = data.get("message")

    db = connect()
    cursor = db.cursor()
    query = "INSERT INTO contact_messages (name, email, subject, message) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name, email, subject, message))
    db.commit()
    cursor.close()

    return jsonify({"status": "success"}), 200

if __name__ == "__main__":
    app.run(debug=True)