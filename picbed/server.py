# coding:utf-8
from flask import Flask, request, jsonify,url_for
import os, time
import hashlib

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/'


def gen_filename(filename):
    file_format = filename.split('.')[-1]
    timestamp = time.time()
    tmp_str = '{}{}'.format(timestamp, filename)
    return (hashlib.md5(tmp_str.encode('utf-8')).hexdigest()) + "." +  file_format

# 上传图片
@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        upload_file = request.files['image001']
        print(upload_file)
        if upload_file:
            filename = gen_filename(upload_file.filename)
           
            if not os.path.exists(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])):
                os.makedirs(os.path.join(app.root_path, app.config['UPLOAD_FOLDER']))
           
            upload_file.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], filename))
            ext_link = url_for('static', filename=filename,  _external=True, _scheme='http')
            return ext_link

@app.route('/static/<string:filename>', methods=['GET'])
def show_photo(filename):
    file_dir = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
    if request.method == 'GET':
        if filename is None:
            pass
        else:
            image_data = open(os.path.join(file_dir, '%s' % filename), "rb").read()
            response = make_response(image_data)
            response.headers['Content-Type'] = 'image/png'
            return response
    else:
        pass

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=10000, debug=True)

