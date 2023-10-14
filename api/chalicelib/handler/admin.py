from chalice.app import Blueprint

from chalicelib.response import response
from chalicelib.application import configer

admin_handler = Blueprint(__name__)
app = admin_handler

@app.route("/hoge2")
def hoge():
    return {'foo': 'barasa'}

@app.route("/toml")
def ptoml():
    ret = configer.show_config()

    return response(ret)
