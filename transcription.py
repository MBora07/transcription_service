from flask import *
from test import transcribe
import os



app = Flask(__name__)


# Set the upload folder
UPLOAD_FOLDER = 'files_uploaded'



@app.route("/")
def home():
    return "HOme"


# Define the upload endpoint
@app.route('/upload', methods=['POST'])
def upload_file():
# Get the uploaded file
    file = request.files['file']

    # Save the file to the upload folder
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Return a success response
    return jsonify({
        'message': 'File uploaded successfully!',
        'filename': file.filename
    })



# Define the transcribe endpoint
@app.route("/transcribe/<filename>", methods=["GET"])
def transcripter(filename):

    # Get the file path
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    # process the file and trying to transcribe
    output_transcription = transcribe(file_path)
    return jsonify(output_transcription)



if __name__ == "__main__":
    port = 3000
    app.run(debug = True, port=port)



    