from flask import Flask, render_template  # , redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

my_email = os.environ.get('MY_EMAIL')

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///projects_database.db')  #
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_type = db.Column(db.String(15), nullable=False)
    title = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(250), unique=True, nullable=False)
    image_url = db.Column(db.String(250), unique=True, nullable=False)
    code_url = db.Column(db.String(250), unique=True, nullable=False)


# db.create_all()


@app.route('/')
def main():
    return render_template('index.html', current_page='index', my_email=my_email)


@app.route('/portfolio')
def portfolio():
    coding_projects = Project.query.filter_by(project_type='coding').all()
    printing_projects = Project.query.filter_by(project_type='printing').all()
    electronic_projects = Project.query.filter_by(project_type='electronics').all()
    all_projects = [coding_projects, printing_projects, electronic_projects]
    return render_template('portfolio.html', all_projects=all_projects, current_page='portfolio')


if __name__ == '__main__':
    app.run(debug=True)
