from flask import Flask, redirect, render_template
from data import state_info, responses, reactions

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html",responses=responses, reactions=reactions)

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/stats")
def stats():
  return render_template("stats.html")

@app.route("/my_state")
def state():
  return render_template("states.html", state_info=state_info)

@app.errorhandler(404)
def page_not_found(e):
  return render_template("404.html"), 404

@app.errorhandler(500)
def internal_server_error():
  return redirect("500.html"), 500

def get_states():
  lines = open("extras/state.txt","r").readlines()
  state_data = {}
  idx = 0
  curr_state = ""
  for line in lines:
    if idx == 0:
      curr_state = line.split(".")[1].strip()
      state_data[curr_state] = []
    else:
      url = ".".join(line.split(".")[1:]).strip()
      state_data[curr_state].append(url)
    idx = (idx + 1) % 3

if __name__ == "__main__":
  get_states()
  app.run(debug=True)
