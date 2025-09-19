import sys
from stats import get_num_words, get_times_chars, sorted_chars

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  
  filepath = sys.argv[1]
  
  book_text = ""
  with open(filepath) as f:
    book_text = f.read()
  
  num_words = get_num_words(book_text)
  count_chars = get_times_chars(book_text)
  sorted_count_chars = sorted_chars(count_chars)

  print("============ BOOKBOT ============")
  print("Analyzing book found at books/frankenstein.txt...")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")
  
  for item in sorted_count_chars:
    print(f"{item["char"]}: {item["num"]}")
  
  print("============= END ===============")

main()