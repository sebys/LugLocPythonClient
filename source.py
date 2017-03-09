import requests

class LugLoc:
  baseUrl = 'https://api.lugloc.com/'
  apiUrl = baseUrl + 'api/'
  username = ""
  password = ""
  client_id = ""
  client_secret = ""

  def __init__(self, username, password, client_id, client_secret):
        self.username = username
        self.password = password
        self.client_id = client_id
        self.client_secret = client_secret
        
  def getToken(self):
      data = {
        "username": self.username,
        "password": self.password,
        "client_id": self.client_id,
        "client_secret": self.client_secret,
        "grant_type": "password" 
      } 

      response = requests.post(self.baseUrl + 'token', data=data).json()
      return response["access_token"]

  def getUserInfo(self):
      url = self.apiUrl + 'account/basicInfo'
      headers = {'Authorization': 'Bearer ' + self.getToken() }
      return requests.get(url, headers=headers).json()

_username = "username@lugloc.com"
_password = "xxxxxxxx"
_client_id = "myclientid"
_client_secret = "myclientsecret"

luglocApiClient = LugLoc(_username, _password, _client_id, _client_secret)
userInfo = luglocApiClient.getUserInfo()


