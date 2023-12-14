from flask import Flask, render_template

from sqlalchemy import create_engine, text
from sqlalchemy.exc import DBAPIError

db_name = "db"
db_user = "username"
db_pass = "password"
db_host = "postgres"
db_port = "5432"
db_string = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
db = create_engine(db_string)

app = Flask(__name__, template_folder="templates")


@app.route("/")
@app.route("/home")
def home():
    markers = [("user-1", [40.748449914335154, -73.98547985091737])]
    return render_template("home.html", markers=markers)


@app.route("/status")
def status():
    running = False
    answer = None
    try:
        connection = db.connect()
        # location of the Empire State building
        lat, lon = 40.748449914335154, -73.98547985091737
        resolution = 5
        result = connection.execute(
            text(f"SELECT h3_lat_lng_to_cell(POINT('{lat},{lon}'), {resolution});")
        )
        answer = result.all()[0][0]
        # answer should be 85f05ab7fffffff
        running = answer == "85f05ab7fffffff"
    except DBAPIError as e:
        app.logger.error(e)
    return render_template("status.html", running=running, answer=answer)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
