from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)
stations = pd.read_csv("/Users/nistha/Documents/Python/Weather-Data-API/data_small/stations.txt", skiprows = 17)
stations = stations[['STAID','STANAME                                 ']]

@app.route("/")
def home():
    return render_template("home.html", data = stations.to_html())

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filename = "/Users/nistha/Documents/Python/Weather-Data-API/data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows = 20, parse_dates=["    DATE"])
    #temperature =23
    temperature = df.loc[df['    DATE']== date]['   TG'].squeeze()/10
    return {"station" : station,
            "date" : date,
            "temperatue" : temperature}


if __name__ == "__main__":
    app.run(debug=True)