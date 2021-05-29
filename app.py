"""
Wymagania:
- jako uzytkownik
    - przegladac najwyzej ocenione filmy (+)
    - przegladac ostatnio dodane filmy
    - ogladac filmy
    - dodawac filmy
    - oceniac filmy
    - komentowac filmy
    - usuwac komentarze
"""


from flask import Flask, render_template
from flask_migrate import Migrate

from db import db
from models.clip import ClipModel

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def index():
    highest_rated = ClipModel.highest_rated(3)

    return render_template(
        'index.html',
        highest_rated=highest_rated,
    )


if __name__ == '__main__':
    app.run()
