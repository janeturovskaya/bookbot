from stats import get_book_stats, count_chars, sorted_d
import sys

def main():
	try:
		path = sys.argv[1]
		words = get_book_stats(path)
		char_counter = count_chars(words)
		sorted_chars = sorted_d(char_counter)
		print("============ BOOKBOT ============")
		print(f"Analyzing book found at {path}...")
		print("----------- Word Count ----------")
		print(f"Found {len(words)} total words")
		print("--------- Character Count -------")
		for key in sorted_chars:
			if key.isalpha():
				print(f"{key}: {sorted_chars[key]}")
		print("============= END ===============")
	except IndexError:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

main()