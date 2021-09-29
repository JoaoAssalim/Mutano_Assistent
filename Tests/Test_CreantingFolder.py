import os
from pathlib import Path

def creatSongFolder():

        directory = Path(os.getcwd() + '\Musics')
        if not os.path.exists(directory):
            os.mkdir(directory)
            print('Creating...')
        else:
            print('Already Exist')
creatSongFolder()