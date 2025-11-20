from flask import Flask, send_from_directory, abort
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)


# 设置你想要的文件目录 (可以是当前目录或者其他目录)
BASE_DIRECTORY = os.getcwd()

@app.route('/<path:filename>', methods=['GET'])
def serve_file(filename):
    # 构建文件路径
    file_path = os.path.join(BASE_DIRECTORY, filename)

    # 检查文件是否存在
    if os.path.isfile(file_path):
        # 通过 send_from_directory 返回文件
        return send_from_directory(BASE_DIRECTORY, filename)
    else:
        # 如果文件不存在，返回 404
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)
