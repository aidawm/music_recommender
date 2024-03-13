import json
import requests

class Mailgun: 
    def __init__(self) -> None:
        data_address = "configs.json"
        f = open(data_address)
        self.configs = json.load(f)
        self.configs = self.configs["mailgun"]

    
    def mail_text (self, music_list):

        text= "Here are recommendation list of musics base on your taste :) :\n"

        for i in range(len(music_list)):
            text = text + "music neme="+music_list[i]["name"]+"\t"+ "artist neme="+music_list[i]["artist"]+"\t"+ "track link="+music_list[i]["link"]+"\n"

        text = text + "hope you enjoy it!"

        return text
    

    def send_email(self,email,music_list):
        return requests.post(
		    self.configs["url"],
		    auth=("api", self.configs["api_key"]),
		    data={"from": self.configs["sender_email"],
		    	"to": [email],
		    	"subject": "music recommendation",
		    	"text": self.mail_text(music_list)})