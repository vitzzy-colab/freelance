from flask import Flask, render_template, request
from model import rekomendasi_freelance

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    if request.method == "POST":
        skills = request.form.get("skills")
        if skills:
            results = rekomendasi_freelance(skills, top_n=5)

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)