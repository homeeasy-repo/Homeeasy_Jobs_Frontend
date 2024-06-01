from flask import Flask, request, render_template, jsonify
import traceback

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        try:
            if 'resume' not in request.files:
                return jsonify({"status": "error", "error": "No file part"}), 400
            
            resume = request.files['resume']
            if resume.filename == '':
                return jsonify({"status": "error", "error": "No selected file"}), 400

            # Save the file or process it here
            # For example: resume.save(os.path.join("uploads", secure_filename(resume.filename)))
            
            # Extract other form data
            first_name = request.form['first-name']
            last_name = request.form['last-name']
            email = request.form['email']
            phone = request.form['phone']
            linkedin = request.form['linkedin']
            city = request.form['city']
            print(first_name,last_name,email,phone,linkedin,city)
            
            # Process the data as needed
            return jsonify({"status": "success"}), 200
        except Exception as e:
            print(f'Error: {e}, Trace: {traceback.format_exc()}')
            return jsonify({"status": "error", "error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)



