import datetime
import uuid

from flask import Flask, request, make_response, render_template, Response

import logging
from flask_cors import CORS

from chain.gen_answer import GenAnswerOfRole

global vectordb
print("第一步")

app = Flask(__name__)
# 设置日志级别
app.logger.setLevel(logging.INFO)

# 创建日志处理器
handler = logging.FileHandler('app.log', encoding='utf-8')
handler.setLevel(logging.INFO)

# 创建日志格式
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# 添加日志处理器到应用程序记录器
app.logger.addHandler(handler)
# from flask_cors import CORS

app = Flask(__name__)

# 允许跨域
CORS(app)



@app.route('/')
def index():
    # return render_template('index.html')
    return "<h1>人类这不是你该来的地方</h1>"

# @app.route('/auto-ppt/gen-uuid', methods=['GET'])
# def get_uuid():
#     random_uuid = str(uuid.uuid4())
#     # todo 将ip地址和uuid 在redis缓存 对话历史记录
    return "<h1>人类这不是你该来的地方</h1>"


@app.route('/generate_answer', methods=("GET", "POST"))
def stream1():
    if request.method == "POST":
        role = request.json["role"]
        uuid = request.json["uuid"]
        query = request.json["query"]
        ip_address = request.remote_addr
        app.logger.info(f'ip地址为 {ip_address}\tuuid为 {uuid}\t作为 {role}\t回答了 {query}')
        title = GenAnswerOfRole(uuid, role)
        return Response(title.query_to_role(query), mimetype='application/octet-stream')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=16000, debug=False, threaded=True)