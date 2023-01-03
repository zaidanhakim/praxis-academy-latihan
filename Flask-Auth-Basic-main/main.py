from flask import Flask, render_template, request, redirect, flash
from flask_login import LoginManager, login_user, UserMixin, current_user, logout_user, login_required
from flask_mongoengine import MongoEngine
from bson import ObjectId

db= MongoEngine()

login_manager = LoginManager()
app = Flask(__name__)
app.config["SECRET_KEY"] = 'rahasia'

login_manager.login_view = 'login'
login_manager.init_app(app)

app.config["MONGODB_SETTINGS"] = [
    {
        "db": "flask_login",
        "host": "localhost",
        "port": 27017,
        "alias": "default",
    }
]
db.init_app(app)

class User(db.Document, UserMixin):
    username = db.StringField(required=True)
    password = db.StringField(required=True)
    is_active = db.BooleanField(default=True)

@login_manager.user_loader
def load_user(user_id):
    return User.objects(id=ObjectId(user_id)).first()

@app.route('/')
@login_required
def dashboard():
    nama = 'bambang'
    return render_template('dashboard.html', nama=current_user.username)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # print(request.method)
    if request.method == 'POST':
        user = request.form.get('user_input')
        password = request.form.get('password_input')
        
        collUser = User.objects(username=user, password=password).first()
        if not collUser:
            flash('User gak ada')
        else:
            login_user(collUser)
            return redirect('/')
    return render_template('login.html')












@app.route('/register', methods=['GET', 'POST'])
def register():
    print(request.method)
    if request.method == 'POST':
        user = request.form.get('user_input')
        password1 = request.form.get('password_input1')
        password2 = request.form.get('password_input2')
        
        if password1 != password2:
            # print("gak cocok")
            flash('Gagal mendaftar')
        else:
            # print(user, password1, password2)
            
            collUser = User(username=user, password=password1)
            collUser.save()
            flash('Silahkan langsung login')
            return redirect('/login')
            
    return render_template('register.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/login')