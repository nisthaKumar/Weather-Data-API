from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("test.html")

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    temperature =23
    return {"station" : station,
            "date" : date,
            "temperatue" : temperature}

@app.route("/Contact/")
def contact_me():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)