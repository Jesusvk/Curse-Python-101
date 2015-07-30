def tipo (adn):
	if type(adn) is str:
		print ('\n' + adn + ' is a string\n')

def sus (w):
	if w == "G":
		return "C"
	elif w == "A":
		return "T"
	elif w == "T":
		return "A"
	elif w == "C":
		return "G"
	return ""

def palabra(siz,b):
	new_word = []
	for a in range(b):
		new_word.append(sus(siz[a]))
	return new_word

"""adn = "gattaca".upper()"""
adn = input ('The word ').upper()
tipo(adn)
word_two = palabra(adn,len(adn))
print ("The complement is \t" + "".join(word_two))
word_two = palabra(adn[::-1],len(adn))
print ("The reverse is \t\t" + "".join(word_two))