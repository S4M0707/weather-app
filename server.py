import flask
import waitress
from weather import get_weather

app = flask.Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return flask.render_template("index.html")

@app.route('/weather')
def get_weather_route():
    city = flask.request.args.get('city')
    weather_data = get_weather(city = city)

    if weather_data['cod'] != 200:
        return flask.render_template(
            'not-found.html',
            title = city
        )

    return flask.render_template(
        "weather.html",
        title = weather_data['name'],
        decription = weather_data['weather'][0]['main'],
        temp = weather_data['main']['temp']
    )

if __name__ == '__main__':
    # waitress.serve(app, host = '0.0.0.0', port = 8000)
    app.run(host = '0.0.0.0', port = 8000)