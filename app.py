from flask import Flask, redirect, render_template
from data import state_info, responses, reactions, testimonials
from stats import stats_info, covid_related

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html",responses=responses, reactions=reactions)

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/stats")
def stats():
  return render_template("stats.html", stats=stats_info, related=covid_related)

@app.route("/info")
def state():
  return render_template("states.html", state_info=state_info)

@app.route("/testimonials")
def tests():
  return render_template("testimonials.html", testimonials=testimonials)

@app.errorhandler(404)
def page_not_found(e):
  return render_template("404.html"), 404

@app.errorhandler(500)
def internal_server_error():
  return redirect("500.html"), 500

if __name__ == "__main__":
  app.run(debug=True)
