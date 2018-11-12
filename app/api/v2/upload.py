import os
from flask import Flask, request
from werkzeug.utils import secure_filename


"""Upload an Image"""

def upload_image(file):
    target_folder = "../static/images"

# check whether the directory exists and try creating if not
    if not os.path.isdir(target_folder):
        os.mkdir(target_folder)

    file = request.files[ 'file']

    if file:
        filename  = secure_filename(file.filename)
        filename.save(os.path.join(target_folder,filename))
