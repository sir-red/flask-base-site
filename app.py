from flask import Flask, url_for, render_template, redirect
from forms import RegistrationForm


app = Flask(__name__, instance_relative_config=False)
app.config.from_object('config.Config')

@app.route('/', methods=('GET', 'POST'))
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        #persist into database
        return redirect(url_for('success'))
    return render_template('index.html', form=form)
