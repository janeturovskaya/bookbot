from collections import Counter

path = 'books/frankenstein.txt'

def get_book_text(path):
	with open(path) as file:
		book_content = file.read()
	return book_content


def get_book_stats(path):
	book_content = get_book_text(path)
	words = book_content.split()
	return words


def count_chars(words):
	words_all_lower = [word.lower() for word in words]
	text = "".join(words_all_lower)
	char_dict = Counter(text)
	return char_dict

def sort_on(items):
	return items["num"]


def sorted_d(char_dict):
	#char_list = [{'char': key, 'num': value} for key,value in char_dict.items()]
	sorted_char_dict = dict(sorted(char_dict.items(), reverse=True, key=lambda item: item[1]))

	return sorted_char_dict