import json
import re


def load_textfile(filename):
    # Open the file
    with open(filename, 'r') as file:
        # Output selected file
        print()
        print("Selected file:", filename)
        print()

        txt = file.read()
        punctuation_marks = {" ", ".", ",", "-", "—", "\"", "\n", "'", \
                             ":", ";", "?", "!", "@", "#", "$", "%", "&", "*"}
        # Remove punctuation marks  and spaces in text
        for character in punctuation_marks:
            txt = txt.replace(character, '')
        # Make text lowercase
        txt = txt.lower()
        return txt


def load_possible_words(filename):
    # Load the selection of english words to search for in decoded text
    with open(filename) as file:
        dct = json.load(file)
    return dct


# Select files
dictionary = load_possible_words('english-dictionary.txt')
text = load_textfile('bible.txt') # -> replace with ozymandias.txt to test Percy Shelley's Ozymandias


def find_matches(txt, search_for):
    # Search for words in decoded text
    p = re.compile('(?=({0}))'.format(search_for))
    matches = re.finditer(p, txt)
    # Print corresponding word along with respective character position in decoded text
    for match in matches:
        print("Match found:", match.group(1), "on position", match.start() + 1)


def decode_message(skip_size, txt):
    line = txt
    result = line[0]
    # Create new string with every n-th character of text (i.e. skip code value)
    for i in range(skip_size, len(line), skip_size):
        result += line[i]
    return result


def find_words_in_cipher(skip_size):
    # Output # of characters in text and words in dictionary to be compared against
    print("Number of characters in text:", len(text))
    print("Number of words in dictionary:", len(dictionary))
    print()

    # Output decoded text using skip code
    print("Decoded text with skip code value of {}:".format(skip_size))
    print(decode_message(skip_size, text))
    print()

    # Look at every word in dictionary for matches in text
    for words in dictionary:
        find_matches(decode_message(skip_size, text), words)


# With a skip code value of for example 10000, run the algorithm on the selected file
find_words_in_cipher(10000)
