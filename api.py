from flask import Flask, request, render_template, jsonify
import traceback
import hashlib
import datetime


app = Flask(__name__)

@app.route("/hiring/resumesubmission", methods=["GET", "POST"])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        try:
            zapier_data = request.get_json(force=True)
            new_candidates = []

            if isinstance(zapier_data, dict):  
                first_name = request.form['first-name']
                last_name = request.form['last-name']
                email = request.form['email']
                phone = request.form['phone']
                linkedin = request.form['linkedin']
                city = request.form['city']
                emailed_on = datetime.now()
                        
                # Hash email to generate indeed_id
                indeed_id = hashlib.sha256(email.encode()).hexdigest()

                # Check if the candidate already exists in the database
                #existing_candidate = IndeedCandidate.query.filter_by(indeed_id=indeed_id).first()

        
                    
                try:
                        fname = first_name.upper()[0] + first_name[1:].lower()
                except IndexError:
                        pass
                    
                try:
                        lname = last_name.upper()[0] + last_name[1:].lower()
                except IndexError:
                        pass
                    
                new_candidate = {
                        'indeed_id': indeed_id,
                        'indeed_email': email,
                        'fname': fname,
                        'lname': lname,
                        'city': city,
                        'alternate_email': None,
                        'phone': phone,
                        'hiring_status_id': 1,
                        'linkedin' : linkedin,
                        'emailed_on': emailed_on,
                    }
                    
                new_candidates.append(new_candidate)
                # Perform bulk insert
                # if new_candidates:
                #     tasks.async_sendActivityEmails.delay(new_candidates, in_person=False)
                #     db.session.bulk_insert_mappings(IndeedCandidate, new_candidates)
                #     db.session.commit()

                return jsonify({"status": "success"}), 200
        except Exception as e:
            print(f'Error: {e}, Trace: {traceback.format_exc()}')
            return jsonify({"status": "error", "error": str(e)}), 400
        

if __name__ == '__main__':
    app.run(debug=True)
