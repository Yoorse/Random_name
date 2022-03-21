import random
from names import *


def generer_navne():

	#randomiserer navne og fornavne
	#random.shuffle(fornavne_list)
	#random.shuffle(efternavne_list)

	navne = []

	#Valg af random navn
	randomnavn = random.choice(fornavne_list)
	randonefternavn = random.choice(efternavne_list)

	#Sammenlægning af randomnavn og randomefternavn
	navne = randomnavn + " " + randonefternavn

	print(navne) 

		

generer_navne()




