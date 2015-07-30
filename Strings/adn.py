def tipo (adn):
	if type(adn) is str:
		print (adn + ' is a string')

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

def palabra(siz):
	new_word = ""
	for a in range(0,len(siz)):
		new_word += sus(siz[a])
	return new_word
def inver(word):
	a = len(word)-1
	b = ""
	while a >= 0:
		b += word[a]
		a -= 1
	return b

		

"""adn = "gattaca".upper()"""
adn = input ('The word ').upper()
tipo(adn)
word_two = palabra(adn)
print ("The complement is " + word_two)
print ("The word in reverse is" + inver(word_two))

