def word(text):
	fh = open(text)

	counter = {}

	for line in fh:
		words = line.strip().split()

		for word in words:
			word = word.strip(",.!?\'\"-:;,").lower()
			try:
				counter[word] += 1
			except KeyError:
				counter[word] = 1
	fh.close()

	word_count = sorted(counter.items(), key=lambda x: x[1], reverse = True)
	f_out = open('dos.txt','w')
	for word,number in counter.items():
		f_out.write("{}: {}\n".format(word,number))


word('uno.txt')