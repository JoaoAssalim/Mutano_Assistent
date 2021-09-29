from bs4 import BeautifulSoup 
import requests 

def show_crypto_price():

	HTML = requests.get("https://coinmarketcap.com/pt-br/currencies/bitcoin/")#requests abre o link e passa para HTML
	soup = BeautifulSoup(HTML.text, 'html.parser')#com o link pega as tags hmtl com informacoes
	text = soup.find("div", attrs={'class':'priceValue smallerPrice'}).text #soup procura a tag que estamos pedindo com a class e .text pega tira as tags html

	return text
print(show_crypto_price())