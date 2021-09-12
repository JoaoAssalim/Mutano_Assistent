import random
from colorama import Fore
from Quest_to_Bot import quests

print(Fore.RED+'''To start, read the possible quests to ask to Mutano on my github: 
https://github.com/JoaoAssalim/Mutanos_Assistent/tree/main/Quest_to_Bot
''')

def tech_quests_assistent():
    file_tech_response = []
    with open('Assistent_learning/tech_response.txt', 'r+') as tech_response:
        for phrase in tech_response:
            file_tech_response.append(phrase)
        tech = random.choice(file_tech_response)
        yield tech

def movie_quests_assistent():
    file_movie_response = []
    with open('Assistent_learning/movie_response.txt', 'r+') as movie_response:
        for phrase in movie_response:
            file_movie_response.append(phrase)
        movie = random.choice(file_movie_response)
        yield movie

def crypto_quests_assistent():
    file_crypt_response = []
    with open('Assistent_learning/crypto_response.txt', 'r+') as crypt_response:
        for phrase in crypt_response:
            file_crypt_response.append(phrase)
        crypto = random.choice(file_crypt_response)
        yield crypto

def games_quests_assistent():
    file_games_response = []
    with open('Assistent_learning/games_response.txt', 'r+') as games_response:
        for phrase in games_response:
            file_games_response.append(phrase)
        games = random.choice(file_games_response)
        yield games

print(Fore.BLUE+"Heeeey, I'm Mutano, your Virtual Assistent!")
name_user = input('What should I call you: ')
print(Fore.YELLOW+f'''
Okay {name_user}, now choose a option in menu:
[1] Talk about technology
[2] Talk about games
[3] Talk about cryptos
[4] Talk about Movies
[0] Turn Off Mutano
''')

choosen_option = input('Chosen option: ')

if choosen_option.isdigit():
    choosen_option = int(choosen_option)

    if choosen_option == 1:
        print(f'Hey {name_user} make me a quest technology! (type "ok" to finish the chat)\n')
        while True:
            quest = input('You: ').lower()
            if quest in quests.tech_quest:
                print(next(tech_quests_assistent()))
            elif quest == 'ok':
                break
            else:
                print('Ask one of the available questions')
                break

    elif choosen_option == 2:
        print(f'Hey {name_user} make me a quest about games! (type "ok" to finish the chat)\n')
        while True:
            quest = input('You: ').lower()
            if quest in quests.games_quest:
                print(next(games_quests_assistent()))
            elif quest == 'ok':
                break
            else:
                print('Ask one of the available questions')
                break

    elif choosen_option == 3:
        print(f'Hey {name_user} make me a quest about crypts! (type "ok" to finish the chat)\n')
        while True:
            quest = input('You: ').lower()
            if quest in quests.crypt_quest:
                print(next(crypto_quests_assistent()))
            elif quest == 'ok':
                break
            else:
                print('Ask one of the available questions')
                break

    elif choosen_option == 4:
        print(f'Hey {name_user} make me a quest about Movies! (type "ok" to finish the chat)\n')
        while True:
            quest = input('You: ').lower()
            if quest in quests.movie_quest:
                print(next(movie_quests_assistent()))
            elif quest == 'ok':
                break
            else:
                print('Ask one of the available questions')
                break
    
    elif choosen_option == 0:
        print(Fore.CYAN+f'See you soon, {name_user}')
    
    else:
        print(Fore.RED+'This number is not in menu!')

else:
    print(Fore.RED+'Enter a number next time!')
             