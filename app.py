from flask import Flask, render_template
from data import state_info

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/my_state")
def state():
  return render_template("states.html", state_info=state_info)

if __name__ == "__main__":
  app.run(debug=True)