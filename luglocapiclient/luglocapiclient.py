# -*- coding: utf-8 -*-
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

    def get_token(self):
        data = {
            "username": self.username,
            "password": self.password,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "password"
            }
        response = requests.post(self.baseUrl + 'token', data=data).json()
        return response["access_token"]

    def get_headers(self):
        return {'Authorization': 'Bearer ' + self.get_token()}

    def get_user_info(self):
        url = self.apiUrl + 'account/basicInfo'
        return requests.get(url, headers=self.get_headers()).json()

    def get_devices(self):
        url = self.apiUrl + 'devices'        
        return requests.get(url, headers=self.get_headers()).json()

    def get_device(self, device_id):
        url = self.apiUrl + 'devices/' + str(device_id)        
        return requests.get(url, headers=self.get_headers()).json()

    def get_location_history(self, device_id, start_date, end_date):
        url = self.apiUrl + 'devices/' + str(device_id) + "/history?startDate=" + start_date + "&endDate=" + end_date        
        return requests.get(url, headers=self.get_headers()).json()

    def refresh_location(self, device_id):
        url = self.apiUrl + 'devices/' + str(device_id) + "/refreshLocation"        
        return requests.post(url, headers=self.get_headers()).json()

    def turn_off(self, device_id, minutes):
        url = self.apiUrl + 'devices/' + str(device_id) + "/turnOff?minutes=" + str(minutes)
        return requests.post(url, headers=self.get_headers()).json()


