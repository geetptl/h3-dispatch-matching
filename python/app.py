from flask import Flask, render_template

from sqlalchemy import create_engine, text

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
    markers = [("user-1", [51.505, -0.09])]
    return render_template("home.html", markers=markers)


@app.route("/status")
def status():
    running = False
    answer = None
    try:
        connection = db.connect()
        lat, lon = 37.3615593, -122.0553238
        result = connection.execute(
            text(f"SELECT h3_lat_lng_to_cell(POINT('{lat},{lon}'), 5);")
        )
        answer = result.all()[0][0]
        # answer should be 85e35e73fffffff
        running = answer == "85e35e73fffffff"
    except Exception as e:
        app.logger.error(e)
    return render_template("status.html", running=running, answer=answer)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
