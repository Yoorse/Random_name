#Liste af fornavne og efternavne

#Åben listen af fornavne og konverter dem til strings
#Derefter tilføjes de til listen fornavne
fornavn = open("fornavne.txt","r")
fornavne = []

for line in fornavn:
	line_strip = line.strip()
	line_split = line_strip.split()
	fornavne.append(line_split)

fornavn.close()

fornavne_list = []

for i in fornavne:
	for j in i:
		fornavne_list.append(j)


#Åben listen af efternavne og konverter dem til strings

efternavn = open("efternavne.txt","r")
efternavne = []

for line in efternavn:
	line_strip = line.strip()
	line_split = line_strip.split()
	efternavne.append(line_split)

efternavn.close()

efternavne_list = []

for i in efternavne:
	for j in i:
		efternavne_list.append(j)



