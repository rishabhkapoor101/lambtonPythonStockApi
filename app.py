from flask import Flask, render_template, request


app=Flask(__name__)

@app.route('/')
def homepage():
    return render_template("./index.html")



@app.route("/stockapp", methods=["POST", "GET"])
def get_weatherdata():
    url="https://api.openweathermap.org/data/2.5/weather"

    company = request.form.get('company')

    import requests
    import json

    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/auto-complete"

    # querystring = params
    querystring = {"q":f"{company}"}


    headers = {
        "X-RapidAPI-Key": "a58f20eb8emshdaf33bc0c1e5185p1a0c38jsn803ce126510f",
        "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }


    response = requests.get(url, headers=headers, params=querystring)
    # data = json.dumps(response.json())
    data = response.json()
    qq1 = data['quotes'][0]['symbol']
    qq2 = data['quotes'][0]['sector']
    qq3 = data['quotes'][0]['industry']

    qq = f"The Ticker of {company} is <b>{qq1}</b> and it is in {qq2} sector in {qq3} industry"
    return qq


if __name__=='__main__':
    app.run(port=7000, debug=True)