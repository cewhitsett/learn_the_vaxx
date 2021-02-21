from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/stats")
def stats():
    return "Hello"

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_server_error():
    return redirect("500.html"), 500

if __name__ == "__main__":
  app.run(debug=True)
