import datetime
from random import choice
import os
from bs4 import BeautifulSoup 
import requests 
import youtube_dl
import time
from pathlib import Path
import shutil
from pygame import mixer



#If user remove or don't got "commands.txt" this func creat a file and add the info there
def commandsFile():
    if not os.path.exists(os.getcwd() + '\commands.txt'):
        creat_file_commands = open('commands.txt', 'w+')
        creat_file_commands.write('-='*35)
        creat_file_commands.write('\n                         COMMANDS TO USE\n')
        creat_file_commands.write('-='*35)
        creat_file_commands.write('\n[0] - STOP PROGRAM\n[1] - SAY WHAT IT THINKS ABOUT CRYPTS\n[2] - GET BITCOIN VALUE HOW MANY COINS YOU WANT\n[3] - DOWNLOAD MUSICS FROM YOUTUBE URL\n[4] - PLAY MUSICS YOU DOWNLOADED\n[5] - STOP PLAYING MUSIC')
        creat_file_commands.close()

    os.system('start commands.txt') #Open NotePad

#If user remove or don't got "dados.txt" this func creat a file and get your name
def dadosFile(): 
    if not os.path.exists(os.getcwd() + '\dados.txt'):
        creat_file_dados = open('dados.txt', 'w+')
        creat_file_dados.close()

    #Verify if "dados.txt" is nule, if is nule it gets your name
    if os.stat("dados.txt").st_size == 0:
        with open('dados.txt', 'a') as dados_get_name:
            name_user = input('Enter Your Name: ')
            dados_get_name.write(name_user)


#Say Good Morning, Afternoon, Night or Dawn for you
def get_time():
    now = datetime.datetime.now()
    hour = now.hour

    #Get Your name in "dados.txt" to use in program
    with open('dados.txt', 'r') as dados_name:
        for line in dados_name:
            name = line


    if hour > 6 and hour < 12:
        return 'Good Morning, ' + name
    elif hour >= 12 and hour < 18:
        return 'Good Afternoon, ' + name
    elif hour >= 18 and hour < 23:
        return 'Good Evening, ' + name
    else:
        return 'Good Dawn, ' + name

#Mutano answer what its thinks about cryptos
def answer_crypt():
    crypts_answers = ['I think Crypts will be the best thing',
    'I think everyplace need accepts crypts as payment',
    'Crypts are the new money',]
    mutano_answer = choice(crypts_answers)
    return mutano_answer


#Show Bitcoin Price
def show_crypto_price():

    HTML = requests.get("https://coinmarketcap.com/pt-br/currencies/bitcoin/")#requests abre o link e passa para HTML
    soup = BeautifulSoup(HTML.text, 'html.parser')#com o link pega as tags hmtl com informacoes
    text = soup.find("div", attrs={'class':'priceValue smallerPrice'}).text #soup procura a tag que estamos pedindo com a class e .text pega tira as tags html

    return text

#If don't exist a Folder Named "Musics" this func will creat
def verifySongFolder(): 

    if not os.path.exists(os.getcwd() + '\Musics'):
        os.mkdir(os.getcwd() + '\Musics')
        print('Creating Folder...\n')

#Download Song from Youtube URL
def download_youtube(link):

    #Formatation to download just audio
    ytb_dl = {
        'format': 'bestaudio/best',
        'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
        }],
    }

    #Verify if is a Youtube/Youtube Music link
    if 'https://www.youtube.com/' in link or 'https://music.youtube.com/' in link:
        print('Downloading...\n')
        time.sleep(1)
        with youtube_dl.YoutubeDL(ytb_dl) as ydl:
            ydl.download([link])
    else:
        print('I cannot download this URL')

#Change Directory's Song to ./Musics
def chanceSongFolder(): 
    Directory = os.getcwd()
    New_Directory = Path(Directory + '\Musics')

    for directory, subfolders, files in os.walk(Directory):
        for file in files:
            if '.mp3' in file:
                song = file
                Old_Directory = os.getcwd() + "\\" + song
                try:
                    shutil.move(Old_Directory,New_Directory)
                except:
                    pass

#Play Song you already downloaded
def playSong():

    directory = os.getcwd()
    Music_Folder = Path(directory + '\Musics')
    SongsToPlay = []

    for FileMain in os.walk(Music_Folder):
        for File in FileMain[2]:
            SongsToPlay.append(File)


    PlayingSong = choice(SongsToPlay)
    print(f'Tocando: {PlayingSong}')
    PlayMusicDirectory = Path(os.getcwd() + '\Musics'+ '\\' + PlayingSong)
        
    mixer.init()
    mixer.music.load(PlayMusicDirectory)
    mixer.music.play()
        
#Pause Song was playing
def pauseSong():
    mixer.music.stop()

    #Execute Every Action in this code
def doActions():
    commandsFile() #Call NotePad File
    dadosFile() #verufy if exist 'dados.txt' and if your name is there
    print(get_time())
    while True:
        option = input("Select a Option: ")

        if option.isdigit(): 
            option = int(option)
            if option == 0:#Break Code
                print('Thanks To Use Me!')
                break
            elif option == 1:#answer about crypts
                print(answer_crypt())
            elif option == 2:#show crypts price
                print(show_crypto_price())
            elif option == 3: #download youtube/youtube music songs
                link = input('Type the Youtube URL: ')
                verifySongFolder() #Creat a Folder named 'Musics' if don't exist
                download_youtube(link) #Download a video from Youtube
                chanceSongFolder() #Change the directory's song
            elif option == 4:#play song you downloaded
                playSong()
            elif option == 5: #stop playing song
                pauseSong()
doActions()