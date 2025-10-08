from flask import Flask, render_template
import random

# pip install flask
app = Flask(__name__)
osebe = ["Ana Novak", "Marko Kovač", "Sara Horvat", "Luka Zupan", "Maja Petek",
    "Jan Kralj", "Tina Bauer", "Matej Bizjak", "Nina Golob", "Peter Novak",
    "Eva Koren", "David Zajc", "Katja Pirc", "Jure Vrh", "Aljaž Rozman",
    "Manca Debeljak", "Gregor Mlakar", "Petra Dolinar", "Žiga Potočnik", "Barbara Šmid",
    "Andrej Zupančič", "Urška Vidmar", "Simona Kos", "Blaž Novak", "Jožef Kovačič",
    "Katarina Bizjak", "Tadej Hribar", "Maja Černe", "David Zupan", "Sara Vidic"
]


@app.route("/")
def hello_world():
    osebe=random.choice(osebe)
    ocena=random.randint(1,5)
    return render_template("index.html", naslov="Najboljsa stran ❤️", 
                           osebe="osebe")


app.run(debug=True)