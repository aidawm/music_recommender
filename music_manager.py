from pydub import AudioSegment
import base64


def split_music(music_file):
    sound = AudioSegment.from_mp3(music_file)
    ten_seconds = 10 * 1000
    x_seconds = 4 * 1000
    music = sound[ten_seconds+x_seconds:ten_seconds+(2*x_seconds)] 
  
    music.export(music_file, format="mp3")

def make_music_mono(music_file):
    stereo_audio = AudioSegment.from_file( 
        music_file, 
        format="mp3") 
    mono_audios = stereo_audio.split_to_mono() 
    mono_left = mono_audios[0].export( 
        music_file, 
        format="mp3") 

def modify_music(id):
    music_file = str(id)+".mp3"

    split_music(music_file)
    make_music_mono(music_file)

def get_base64(id):
    music_file = str(id)+".mp3"
    sound = AudioSegment.from_mp3(music_file)
    base64_str = base64.b64encode(sound._data).decode("utf-8")
    return base64_str





    
