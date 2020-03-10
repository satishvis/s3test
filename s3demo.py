import os
from flask import Flask, render_template, request, redirect, \
    send_file, flash, url_for
# from s3_demo import list_files, download_file, upload_file, delete_file
from s3_demo import S3
from werkzeug.utils import secure_filename
from config import S3_KEY, S3_SECRET, BUCKET


UPLOAD_FOLDER = "uploads"
SECRET_KEY = "12345"

app = Flask(__name__)
# BUCKET = os.getenv("BUCKET")
app.config['SECRET_KEY'] = SECRET_KEY

# @app.route('/')
# def entry_point():
#     return 'Hello World!'
s3 = S3(S3_KEY, S3_SECRET)


@app.route('/')
@app.route("/storage")
def storage():
    contents = s3.list_files(BUCKET)
    return render_template('storage.html', contents=contents)


@app.route("/upload", methods=['POST'])
def upload():
    if request.method == "POST":
        if 'files[]' not in request.files:
            flash('No file part')
        files = request.files.getlist('files[]')
        for f in files:
            f.save(os.path.join(UPLOAD_FOLDER, secure_filename(f.filename)))
            s3.upload_file(UPLOAD_FOLDER+'/'+f"{f.filename}", BUCKET)
            flash(f"File {f.filename} Uploaded to S3")

    return redirect(url_for("storage"))


@app.route("/download/<filename>", methods=['GET'])
def download(filename):
    if request.method == 'GET':
        output = s3.download_file(filename, BUCKET)

        return send_file(output, as_attachment=True)


@app.route("/delete/<filename>", methods=['GET'])
def delete(filename):
    if request.method == 'GET':
        s3.delete_file(filename, BUCKET)
        flash(f'{filename} deleted')
    # return redirect("/storage")
    return redirect(url_for("storage"))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
