from flask import *
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route('/')
def home():
    return render_template(
        'index.html',
        styles=url_for('static', filename='dist/output.css'),
        plantimg=url_for('static', filename='plant.png')
        )


@app.route('/login')
def login():
    return render_template(
        'login.html',
        styles=url_for('static', filename='tailwindstyles.css'),
        )


if __name__ == '__main__':
    app.run(debug=True)
