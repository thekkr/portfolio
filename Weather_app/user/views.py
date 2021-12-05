from flask import Blueprint,redirect,render_template,request,url_for
from Weather_app.user.forms import LoginForm,RegisterForm,UpdateForm
from Weather_app.models import User
from Weather_app import app,db
from flask_login import login_user,logout_user,current_user,login_required

users = Blueprint('users',__name__)
ALLOWED_EXTENSIONS = ['jpg','png','jpeg']

def allowed_file(filename):
    return '.' in  filename and filename.split('.',1)[1] in ALLOWED_EXTENSIONS
#logout

@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('core.index'))

#Login
@users.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            print('yes')
            next = request.args.get('next')
            if next==None or next[0]=='/':
                next = url_for('users.account')
            return redirect(next)
    return render_template('login.html',form=form)

#Registration

@users.route('/register',methods=['GET','POST'])
def register():

    form = RegisterForm()

    if form.validate_on_submit():

        user = User(username = form.username.data,email=form.email.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('users.login'))
    return render_template('register.html',form=form)

@users.route('/account')
def account():

    form = UpdateForm()

    if form.validate_on_submit():

        picture = request.files['picture']

        if picture and allowed_file(picture.filename):
            filename = str(current_user.username)+'.'+picture.filename.split('.',1)[1]
            picture.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            current_user.profile_image=filename

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    profile_image = url_for('static',filename='profile_images/'+current_user.profile_image)
    return render_template('account.html',profile_image=profile_image,form=form)
