import sys
from stats import *

def get_book_text(file):
	try:
		with open(file) as f:
			file_contents = f.read()
		return file_contents
	except Exception as e:
		print(e)
		sys.exit(1)

def main():
	#filepath = "books/frankenstein.txt"
	try:
		filepath = sys.argv[1]
	except:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	print_report(get_book_text(filepath),filepath)
main()
