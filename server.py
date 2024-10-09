from flask import Flask, request, render_template, redirect, url_for, send_from_directory, flash
from werkzeug.utils import secure_filename
import os
from PIL import Image

app = Flask(__name__, static_folder="public")
app.secret_key = "yoyo"
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = './uploads'
app.config['THUMBNAIL_FOLDER'] = 'static/thumbnails'
app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'jpeg', 'png', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

session = {
    "authenticated": False,
    "username": None,
}

ALLOWED_USERS = {
    "Admin": "top_secret",
    "UserOne": "One123",
    "Hacker": "IA1RULZZ!"
}

@app.route("/")
def home():
    return render_template('home.html', authenticated=session["authenticated"], username=session["username"])

@app.route("/gallery", methods=['GET'])
def gallery():
    people = []
    travel= []
    animal = []
    nature = []
    k = 0
    for root, dirs, files in os.walk(UPLOAD_FOLDER):
        k = k + 1
        for file in files:
            if file.endswith(('jpg', 'jpeg', 'png', 'gif')):
                relative_path = os.path.join(root, file)
                url_path = os.path.relpath(relative_path, UPLOAD_FOLDER).replace("\\", "/")
                if k == 2:
                    people.append(url_path)
                elif k == 3:
                    nature.append(url_path)
                elif k == 4:
                    travel.append(url_path)
                elif k == 5:
                    animal.append(url_path)
    return render_template('gallery.html', people=people, travel=travel, nature=nature, animal=animal, authenticated=session["authenticated"], username=session["username"])

@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            category = request.form.get('category')
            if not category:
                flash('No category selected')
                return redirect(request.url)

            category_folder = os.path.join(app.config['UPLOAD_FOLDER'], category)
            if not os.path.exists(category_folder):
                os.makedirs(category_folder)

            value = request.form.getlist('check')
    
            filename = file.filename

            if not value:
                file.save(os.path.join(category_folder, filename))
            else:
                img = Image.open(file)
                grayscale_image = img.convert("L")
                grayscale_image.save(os.path.join(category_folder, filename))
            
            flash('File successfully uploaded')
            return redirect('/gallery')
    return render_template('upload.html', authenticated=session["authenticated"], username=session["username"])


@app.route("/aboutus")
def about():
    return render_template('aboutus.html', authenticated=session["authenticated"], username=session["username"])

@app.route("/login", methods=["GET", "POST"])
def login():
    error_msg = None
    if request.method == "POST":

        username = request.form.get("username", "")
        password = request.form.get("password", "")

        if username in ALLOWED_USERS and ALLOWED_USERS[username] == password:
            session['authenticated'] = True
            session['username'] = username
            return redirect('/')
        else:
            error_msg = "Incorrect username or password"
            
    return render_template("login.html", error_msg=error_msg)
   

@app.route("/logout")
def logout():
    session["authenticated"] = False
    session["username"] = None
    return redirect('/')

@app.route("/vreaumarire")
def marire():
    return render_template('vreau_marire.html')

@app.errorhandler(404)
def error404(code):
    return "HTTP Error 404 - Page Not Found"

if __name__ == "__main__":
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True, port=5000)

