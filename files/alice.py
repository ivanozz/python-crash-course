def count_words(filename):
	"""подсчет приблизительного количества слов в тексте"""
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		# or pass
		msg = "Sorry, the file " + filename + " does not exist"
		print(msg)
	else:
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) + " words")

filename = 'alice.txt'
count_words(filename)

filenames = ['alice.txt', 'siddhartha.txt', 'mobi_dick.txt', 'little_women.txt']
for filename in filenames:
	count_words(filename)
