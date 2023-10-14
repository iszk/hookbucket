from chalice.app import Blueprint

user_handler = Blueprint(__name__)

@user_handler.route("/hoge")
def hoge():
    return {'foo': 'bar'}

