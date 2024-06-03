from flask import Flask, request, jsonify
from flask_cors import CORS
import traceback
import hashlib
import datetime

app = Flask(__name__)
CORS(app)

@app.route("/hiring/resumes", methods=["POST", "GET"])
def index():

    if request.method == "POST":
        try:
            # zapier_data = request.get_json(force=True)
            # new_candidates = []

            # if isinstance(zapier_data, dict):
            first_name = request.form['first-name']
            last_name = request.form['last-name']
            email = request.form['email']
            phone = request.form['phone']
            linkedin = request.form['linkedin']
            city = request.form['city']
            emailed_on = datetime.datetime.now()

            # Hash email to generate indeed_id
            indeed_id = hashlib.sha256(email.encode()).hexdigest()

            try:
                fname = first_name.upper()[0] + first_name[1:].lower()
            except IndexError:
                fname = first_name

            try:
                lname = last_name.upper()[0] + last_name[1:].lower()
            except IndexError:
                lname = last_name

            new_candidate = {
                'indeed_id': indeed_id,
                'indeed_email': email,
                'fname': fname,
                'lname': lname,
                'city': city,
                'alternate_email': None,
                'phone': phone,
                'hiring_status_id': 1,
                'linkedin': linkedin,
                'emailed_on': emailed_on,
                }

            print(new_candidate)
            received_Data = new_candidate
            # Perform bulk insert
            # if new_candidates:
            #     tasks.async_sendActivityEmails.delay(new_candidates, in_person=False)
            #     db.session.bulk_insert_mappings(IndeedCandidate, new_candidates)
            #     db.session.commit()
        
            return jsonify({"status": "success"}), 200
        except Exception as e:
            print(f'Error: {e}, Trace: {traceback.format_exc()}')
            return jsonify({"status": "error", "error": str(e)}), 400

    if request.method == "GET":
        if received_Data is None:
            return jsonify({"status": "error", "message": "No data available"}), 400
        return jsonify({'data': received_Data}), 200
        # return jsonify({"status": "success"}), 200
    # except Exception as e:
    #     print(f'Error: {e}, Trace: {traceback.format_exc()}')
    #     return jsonify({"status": "error", "error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)