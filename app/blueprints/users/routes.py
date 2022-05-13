from crypt import methods
import email
from flask import render_template, current_app as app, request, redirect, url_for, flash
from app.blueprints.users.models import Post
from app.blueprints.users.models import User
from flask_login import login_user, logout_user 


# USER ROUTES
@app.route('/users')
def users():
    return render_template('users/users.html')

@app.route('/profile', methods=['GET','POST'])
def profile():
    if request.method == 'POST':
        data = request.form.get('poke_post')

        flash('Here is your pokemon', 'warning')
        return redirect(url_for('profile'))
    return render_template('users/profile.html', posts=[post.to_dict() for post in Post.query.order_by(Post.date_created.desc()).all()])

@app.route('/users/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        form_data = request.form
        user = User.query.filter_by(email=form_data.get('email')).first()


        # checking user email validity and password
        user = User.query.filter_by(email=form_data.get('email')).first()
        if user is None or not user.check_password(form_data.get('password')):
            flash('The email address or password doesn\'t exist, please try again', 'danger')
            return redirect(url_for('login'))

        # log the user in
        login_user(user, remember=form_data.get('remember_me'))
        
        flash('You have logged in successfully', 'success')
        return redirect(url_for('home'))
    return render_template('users/login.html')

@app.route('/users/logout')
def logout():
    logout_user()
    flash('You have logged out successfully', 'primary')
    return redirect(url_for('login'))

@app.route('/users/sign_up')
def sign_up():
    return render_template('users/sign_up.html')