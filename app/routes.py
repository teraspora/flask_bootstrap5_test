from flask import render_template
from app import app


users = {
    'john': {
        'id': '3722',
        'name': 'John'
    },
    'loop': {
        'id': '4896',
        'name': 'Loop'
    },
    'zest': {
        'id': '103',
        'name': 'Zest'
    },
    'rind': {
        'id': '664',
        'name': 'Rind'
    },
    
}

@app.route('/index')
@app.route('/')
@app.route('/<name>')
def index(name='john'):
    user = users.get(name)
    return render_template('index.html', title='Raccoons and Cement', user=user)
