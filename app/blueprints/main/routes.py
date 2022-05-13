from flask import render_template, current_app as app
from flask_login import current_user
# MAIN ROUTES
@app.route('/')
def home():
    print(current_user)
    return render_template('main/home.html')

@app.route('/about')
def about():
    return render_template('main/about.html')