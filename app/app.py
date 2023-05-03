from flask import Flask, request, render_template, redirect, flash
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")

app = Flask(__name__, template_folder="templates")
app.secret_key = "$u$$y"
app.config["UPLOAD FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def groove_street():
    return render_template("home.html")

@app.route('/upload')
def upload_file():
    return render_template("upload.html")

@app.route('/uploader', methods=['POST'])
def uploader_file():
    if request.method == "POST":
        f = request.files["file"]
        f.save(os.path.join(app.config["UPLOAD FOLDER"], secure_filename(f.filename)))
        flash("File uploaded successfully!")
        return redirect("/")
    
    
if __name__ == "__main__":
    app.run(debug=True)

