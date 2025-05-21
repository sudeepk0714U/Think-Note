from flask import Blueprint, render_template,request,flash,redirect,url_for
from .models import User
from . import db
from werkzeug.security import check_password_hash,generate_password_hash
from flask_login import login_user,login_required,logout_user,current_user


auth = Blueprint('auth',__name__)
@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password,password):
                flash("Logged in Successfully! 😀", category='success')
                login_user(user,remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Incorrect Password! 🧐",category="error")
        else: 
            flash("Email Does not Exist! 🧐" , category='error') 
    return render_template("login.html",text = "hello world",user=current_user)




@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login')) 




@auth.route('/sign-up',methods=['GET','POST']) 
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2') 
        user = User.query.filter_by(email=email).first()
        if user:
            flash("User aldready exists! 🧐",category='error') 
        elif len(email)<4:
            flash("Length of the email should be greater than 4 charachters",category="error")
        elif len(firstname)<2:
            flash("Length of the first name should be greater than 2 charachters",category="error")
        elif len(password1) < 8: 
            flash("Password should be of atleast 8 charachters",category="error")
        elif password1 != password2:
            flash("Both the password do not match",category="error")
        else: 
            new_user = User(email = email,firstname=firstname,password=generate_password_hash(password1,method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()  
            login_user(user,remember=True)
            flash("Account created successfully!",category="success") 
            return redirect(url_for('views.home')) 
        # add usr to database

    return render_template("sign_up.html",user=current_user)  