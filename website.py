# import config
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def webpage():
    # direction = config.direction
    direction = "Up"
    return render_template("game.html", direction=direction)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
