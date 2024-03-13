import requests 
import json


class Shazam:

    def __init__(self) -> None:
        data_address = "configs.json"
        f = open(data_address)
        self.configs = json.load(f)
        self.configs = self.configs["rapidapi"]

        self.url = "https://shazam.p.rapidapi.com/songs/detect"
        self.querystring = {"timezone":"America/Chicago","locale":"en-US"}

        self.headers = {
        	"content-type": self.configs["content-type"],
        	"X-RapidAPI-Key": self.configs["X-RapidAPI-Key"],
        	"X-RapidAPI-Host": self.configs["shazam-RapidAPI-Host"]
        }

    def detect(self,music):
        response = requests.post(self.url, data=music, headers=self.headers, params=self.querystring)
        response_json = response.json()
        # print(response_json)
        # print(response_json.keys())
        title = response_json["track"]["share"]["subject"]
        return title

