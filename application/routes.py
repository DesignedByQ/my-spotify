from application import app
from application import db




@app.route('/')
def index():
    todo = 'Connected'
    return todo



