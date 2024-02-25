import configparser
import requests

def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']

def get_weather_results(zip_code, api_key):
    api_url = "https://api.openweathermap.org/data/2.5/weather?zip={}&appid={}".format(zip_code,api_key)
    print(api_url)
    r = requests.get(api_url)
    return r.json()

print(get_weather_results("95129",get_api_key()))


function addNewTransaction(ev) {
    ev.preventDefault();
    const url = process.env.REACT_APP_API_URL + '/transaction';
    //const url = "http://localhost:4000/api" + "/transaction";
    fetch(url,{
      method: 'POST',
      headers: {'Content-type': 'application/json'},
      body: JSON.stringify({name,description,datetime})
    }).then(response => {
      response.json().then(json => {
        console.log('result', json);
      });
    });
  }
