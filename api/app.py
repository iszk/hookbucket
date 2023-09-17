from typing import List

from chalice.app import Chalice, Rate, Cron

from chalicelib import handler

app = Chalice(app_name='hookbucket-backend')
app.register_blueprint(handler.user_handler)
app.register_blueprint(handler.admin_handler)

@app.route('/')
def index():
    return {'hello': 'world'}
