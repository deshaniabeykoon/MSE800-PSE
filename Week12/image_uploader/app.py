from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join('static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB limit

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html', uploaded_filename=None)

@app.route('/uploads', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return 'No file part'
    
    file = request.files['image']

    if file.filename == '':
        return 'No selected file'

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # Ensure folder exists
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        file.save(filepath)
        
        return render_template('index.html', uploaded_filename=filename)
        # Uncomment the following lines if you want to save the file and redirect
        # to a display page
        #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #return redirect(url_for('display_image', filename=filename))
    
    return 'File type not allowed'

@app.route('/display/<filename>')
def display_image(filename):
    return render_template('display.html', filename=filename)

if __name__ == '__main__':
    app.run(debug=True)
