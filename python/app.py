from flask import Flask

from sqlalchemy import create_engine, text

db_name = 'db'
db_user = 'username'
db_pass = 'password'
db_host = 'postgres'
db_port = '5432'
db_string = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
db = create_engine(db_string)

app = Flask(__name__)


@app.route('/status')
def status():
    try:
        connection = db.connect()
        result = connection.execute(text("SELECT h3_lat_lng_to_cell(POINT('37.3615593,-122.0553238'), 5);"))
        answer = result.all()[0][0]
        # answer should be 85e35e73fffffff
        return f"<p>Dispatch matching application is running.</p><p style='font-size:10'>{answer}</p>"
    except Exception as e:
        app.logger.error(e)
        return "Unable to reach database."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
