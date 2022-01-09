from flask import render_template
from app import app


user = {
    'id': '3722',
    'name': 'John'
}

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Raccoons and Cement', user=user)
