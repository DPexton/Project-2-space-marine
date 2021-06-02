  
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import requests
from os import getenv
from sqlalchemy import desc

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')

db = SQLAlchemy(app)

class Marine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chapter = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(50), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():

    chapter = requests.get("http://service-2:5001/chapter")

    role = requests.get("http://service-3:5002/role")

    name = requests.post("http://service-4:5003/name", data=result)
    result = str(chapter.text) + " " + str(role.text)

    return render_template(
        'layout.html', 
        title= 'Home', 
        role=role.txt, 
        chapter=chapter.txt, 
        result=result, 
        name=name.text
        )
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port= 5000)