from chalice.app import Blueprint

admin_handler = Blueprint(__name__)
app = admin_handler

@app.route("/hoge2")
def hoge():
    return {'foo': 'barasa'}

