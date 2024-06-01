from flask import Flask, request, render_template, jsonify
import traceback
from datetime import datetime
import hashlib
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route("/hiring/resumesubmission", methods=["GET", "POST"])
def index():
    if request.method == 'GET':
        return render_template('jobs.html')
    elif request.method == 'POST':
        try:
            first_name = request.form['first-name']
            last_name = request.form['last-name']
            email = request.form['email']
            phone = request.form['phone']
            linkedin = request.form['linkedin']
            city = request.form['city']
            emailed_on = datetime.now()
                    
            # Hash email to generate indeed_id
            indeed_id = hashlib.sha256(email.encode()).hexdigest()

            # Here, you would typically interact with your database
            # For example: Check if the candidate already exists in the database
            # existing_candidate = IndeedCandidate.query.filter_by(indeed_id=indeed_id).first()

            # Simulating adding a new candidate
            new_candidate = {
                'indeed_id': indeed_id,
                'email': email,
                'first_name': first_name,
                'last_name': last_name,
                'city': city,
                'phone': phone,
                'linkedin': linkedin,
                'emailed_on': emailed_on,
            }

            # Here you would typically save to your database

            return jsonify({"status": "success", "candidate": new_candidate}), 200
        except Exception as e:
            print(f'Error: {e}, Trace: {traceback.format_exc()}')
            return jsonify({"status": "error", "error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
