from logger import logger
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os
import localsftp


app = Flask(__name__)
logger.debug("debug message")
logger.info("info message")
logger.warning("warning message")
logger.error("error message")
logger.critical("critical message")

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = os.environ.get('MY_SECRET')
@app.route('/', methods=['POST', 'GET'])
def homepage():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():

    if request.method == 'POST':
        file = request.files['file']
        filepath=f"./files/{secure_filename(file.filename)}"
        filename=f"{secure_filename(file.filename)}"
        file.save(filepath)
        logger.log(10, "File saved to %s", filepath)
        sftp = localsftp.get_sftp()
        if file:
            with sftp:
                with sftp.cd('/uploads'):
                    sftp.put(filepath)
                    sftp.get(filename)
            return "Upload Success!"
        else:
            return "no file found"
    if request.method== 'GET':
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)