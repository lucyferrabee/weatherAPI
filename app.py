from flask import Flask, render_template, request
import requests

app = Flask(__name__)
api_key = '60e40e0879a04264aff135647230205'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    url = f'https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no'
    response = requests.get(url).json()
    temperature = response['current']['temp_c']
    condition = response['current']['condition']['text']
    return render_template('weather.html', city=city, temperature=temperature, condition=condition)

if __name__ == '__main__':
    app.run(debug=True)
