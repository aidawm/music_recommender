import rabbitmq_manager 
from s3_manager import S3
from music_manager import *
from shazam_manager import Shazam
from spotify_manager import Spotify
from database_manager import DB

file_storage = S3()
shazam = Shazam()
spotify = Spotify()
db = DB()

def notify(id):

    id = int(id)
    print(id)
    file_storage.get_object(id)
    modify_music(id)
    data = get_base64(id)
    music_title = shazam.detect(data)
    print(music_title)
    music_id = spotify.search(music_title)
    print(music_id)

    db.set_songID(id,str(music_id))
    db.set_status(id , 'ready')


    file_storage.delete_object_from_local(id)










if __name__ == '__main__':
    amqp = rabbitmq_manager.AMQP()
    amqp.recieve_message()

    
    

