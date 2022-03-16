import random
from names import *


def generer_navne():

	random.shuffle(fornavne_list)
	random.shuffle(efternavne_list)

	navne = []



	randomnavn = random.choice(fornavne_list)
	randonefternavn = random.choice(efternavne_list)

	navne = randomnavn + " " + randonefternavn

	print(navne) 

		

generer_navne()




