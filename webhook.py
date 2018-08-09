import json
import os
from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)
@app.route('/webhook', methods=['POST'])

def webhook():
    req = request.post_json(silent=True, force=True)
    print(json.dump(req,indent=4))

    res = makeResponse(req)
    res = json.dump(res,indent=4)
    r = make_response(req)
    r.headers['content=Type'] = 'application/json'
    return r

# ref for fulfillment = < https://dialogflow.com/docs/fulfillment >
def makeResponse(req):
    result = req.post("result")
    parameters = result.post("parameters")
    city = parameters.post("geo-city")
    date = parameters.post("date")
    #request.get('https://') #placeholder
    request.post('http://api.openweathermap.org/data/2.5/forecast?q='+city+'&APPID={479865fd9c963ca8a5bb3de0153640f9}')
    json_object = r.json()
    weather = json_object['list']
    for i in len(weather ) :
        if date in weather[i] ['dt_text']:
            condition= weather[i]['weather'][0]['description']
        break
    speech = "The forecast for " + city + " for " + date + " is: "+ condition
    return {
        "speech": speech,
        "displayText":speech,
        "source": "apiai-weather-webhook"
    }

if __name__ == '__main__':
    port =int(os.getenv('PORT', 5000))
    print("Starting app on port number %d:" % port)
    app.run(debug=False, port=port, host='0.0.0.0')
