import os
from pathlib import Path
from random import choice
from pygame import mixer

def playAndStopSong():

    pasta = os.getcwd()
    Music_Folder = Path(pasta + '\Musics')
    SongsToPlay = []

    for FileMain in os.walk(Music_Folder):
        for File in FileMain[2]:
            SongsToPlay.append(File)

    PlayingSong = choice(SongsToPlay)
    print(PlayingSong)
    print(f'Tocando: {PlayingSong}')
    PlayMusicDirectory = Path(os.getcwd() + '\Musics'+ '\\' + PlayingSong)
            
    mixer.init()
    mixer.music.load(PlayMusicDirectory)
    mixer.music.play()
        
    stop_playing_song = input('Press Enter to Stop: ')

    if stop_playing_song == '' or stop_playing_song != '':
        mixer.music.pause()
playAndStopSong()