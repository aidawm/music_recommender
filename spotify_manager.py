import requests
import json


class Spotify:

    def __init__(self) -> None:
        data_address = "configs.json"
        f = open(data_address)
        self.configs = json.load(f)
        self.configs = self.configs["rapidapi"]
        
        

        self.headers = {
        	"X-RapidAPI-Key": self.configs["X-RapidAPI-Key"],
        	"X-RapidAPI-Host": self.configs["spotify-RapidAPI-Host"]
        }


    def search(self,query):
        url = "https://spotify23.p.rapidapi.com/search/"
        querystring = {"q":f"{str(query)}","type":"tracks","offset":"0","limit":"10","numberOfTopResults":"5"}
        # print(self.querystring)
        response = requests.get(url, headers=self.headers, params=querystring)
        # print(response)
        response_json = response.json()
        print(response_json.keys())
        # ["items"]["data"]["id"]
        return response_json["tracks"]["items"][0]["data"]["id"]
        # title = response_json["share"]["subject"]
        # return title


    def recommend_music(self,music_id):
        
        url = "https://spotify23.p.rapidapi.com/recommendations/"

        querystring = {"limit":"5","seed_tracks":music_id}

        response = requests.get(url, headers=self.headers, params=querystring)
        response = response.json()

        music_list = []

        tracks = response["tracks"]
        for i in range(len(tracks)):
            t = tracks[i]
            # , "artist":t["artists"]["name"] , "link" : t["external_urls"]["spotify"]
            music_list.append({"name":t["name"] ,"artist":t["artists"][0]["name"] , "link" : t["external_urls"]["spotify"]})


        return music_list
        
        