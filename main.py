import sys
from stats import get_num_words, get_character_analysis, sort_stats

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)
    num_words = get_num_words(text)
    char_stats = get_character_analysis(text)

    print_report(path, num_words, char_stats)


def get_book_text(path_to_file: str):
    with open(path_to_file) as file:
        file_contents = file.read()
    return file_contents


def print_report(path_to_book, num_words, occurence_dict):
    # Remove non alphanumeric chars and sort descending
    char_occurence = sort_stats(occurence_dict)
    char_occurence = list(filter(lambda x: x[0].isalpha(), char_occurence))

    print("============ BOOKBOT ============")
    print(f"Analysing book foud at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for c in char_occurence:
        print(f"{c[0]}: {c[1]}")

    print("============= END ===============")


main()