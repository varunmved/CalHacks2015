import os
import requests
from flask import Flask,request,g

app = Flask(__name__)
app.config['DEBUG'] = True
CLIENT_ID = "7SVJKHGaapdeAfV5qCD0m88amCJ8xmaz8Psj9hov"
CLIENT_SECRET = "Cr8vetDkTMSkZDPfmSvwLYlty0aYDpbElwCui3NzTnjC4rJI3K"
SERVER_URL = "https://api.lumobodytech.com"
REDIRECT_URI = 'http://localhost:8000/authorized/'

@app.route('/authorized/',methods=['GET','POST'])
def exchange_code_for_access_token():
    print request.args.get('code')
    print request.json

    authorization_code = request.args.get('code')
    data={'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'code':authorization_code,
            'grant_type':'authorization_code',
            'redirect_uri': REDIRECT_URI}

    token_url = '%s/oauth2/token/' % SERVER_URL
    print "fetching token from ",token_url
    result = requests.post(token_url,data=data)
    print result.content
    print result.reason
    print result.status_code
    g.refresh_token = result.json()['refresh_token']
    return "OK"

@app.route('/refresh/',methods=['GET','POST'])
def use_refresh_token():
    data={'client_id': CLIENT_ID,
            'client_secret' : CLIENT_SECRET,
            'refresh_token' : g.refresh_token,
            'grant_type':'refresh_token'
            }
    token_url = '%s/oauth2/token/' % SERVER_URL
    print "refreshing token from ",token_url
    result = requests.post(token_url,data=data)
    print result.content
    print result.reason
    print result.status_code
    return result.content

if __name__ == '__main__':
    port = int(os.environ.get('PORT',8000))
    app.run(host='0.0.0.0',port=port,debug=True)
