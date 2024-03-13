import time, threading 
from database_manager import DB
from spotify_manager import Spotify
from mailgun_manager import Mailgun

db = DB()
spotify = Spotify()
mail = Mailgun()

def get_data_from_db():

    print(time.ctime())
    new_requests = db.show_ready_requests()
    print(new_requests)
    if (len(new_requests)>0):
        for i in range(len(new_requests)):
            music_list = spotify.recommend_music(new_requests[i][3])
            
            mail.send_email(new_requests[i][1],music_list)

            db.set_status(new_requests[i][0],"done")

    threading.Timer(30, get_data_from_db).start()


get_data_from_db()