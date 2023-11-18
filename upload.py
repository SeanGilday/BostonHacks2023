# upload.py
# Author: Stavros Constantinou
#
# Creating an upload system that will allow files to be uploaded.
from flask import Flask, render_template, request
import os
import traceback

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('uploadButton.html')

@app.route('/upload', methods=['POST'])
def upload():
    try:
        if 'file' not in request.files:
            return 'No file part'

        file = request.files['file']

        if file.filename == '':
            return 'No selected file'

        if file and allowed_file(file.filename):
            destination = os.path.join('uploads', file.filename)
            print("Destination Path:", destination)

            if not os.path.exists('uploads'):
                os.makedirs('uploads')

            file.save(destination)
            return 'File uploaded successfully'

        return 'Invalid file type. Allowed file types are: txt, pdf, png, jpg, jpeg, gif'
    except Exception as e:
        print("Exception:", str(e))
        print("Traceback:", traceback.format_exc())
        return 'An error occurred during file upload.'

if __name__ == '__main__':
    app.run(debug=True)




