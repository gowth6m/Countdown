# COUNTDOWN
# coding: utf-8
import itertools
import random

# Name of the file being used as the dictionary.
DICTIONARY_FILE = 'words.txt'


def remove_repeats(list_of_winning_words):
    """ Removes repeated words in the list. """
    final_list = []
    for word in list_of_winning_words:
        if word not in final_list:
            final_list.append(word)
    return final_list


def select_characters():
    """ Asks the user to input a ’c’ for a consonant or a ’v’ for a vowel nine times and
    returns a string with the corresponding number of random consonant and vowel characters. """
    random_string = []
    vowels = 'eeeeeeeeeeeeeeeeeeeeeaaaaaaaaaaaaaaaiiiiiiiiiiiiiooooooooooooouuuuu'
    consonants = 'bbcccddddddffggghhjklllllmmmmnnnnnnnnppppqrrrrrrrrrssssssssstttttttttvwxyz'
    list_of_vowels = list(vowels)
    list_of_consonants = list(consonants)
    # loop for taking in user input and giving out C and V.
    i = 0
    while i < 9:
        user_input = input('Enter c for a consonant and v for vowel: ')
        if user_input == 'c' or user_input == 'C':
            random_string.append(random.choice(list_of_consonants))
            i += 1
        elif user_input == 'v' or user_input == 'V':
            random_string.append(random.choice(list_of_vowels))
            i += 1
        else:
            print('Invalid!')
    # joins the letters in the list into one string.
    new_string = ''.join(map(str, random_string))
    return new_string


def dictionary_reader(file_name):
    """ Takes a string argument containing a filename, the function opens the relevant file,
    iterate through each line to create a list of the words in the file and return the list. """
    file_name = str(file_name)
    with open(file_name, "r") as read_file:
        # Splitting the words in the file on each new line.
        list_of_words = read_file.read().split('\n')
    read_file.close()
    return list_of_words


def word_lookup(letters):
    """ Takes a string argument. The function checks if the characters in the string are contained in any of the words
    in the text file. Returns the longest possible word and all words with that length. """
    dictionary = dictionary_reader(DICTIONARY_FILE)
    list_of_winning_words = []
    small_dictionary = []
    sorted_small_dictionary = []
    # Creates a smaller dictionary by removes words that are too long.
    for word in dictionary:
        if len(word) <= len(letters):
            small_dictionary.append(word)
    # Sorts the words in the dictionary in alphabetical order.
    for word in small_dictionary:
        sorted_small_dictionary.append("".join(sorted(word)))
    # Sorts the random letters in alphabetical order.
    sorted_word = "".join(sorted(letters))
    isFound = False
    for i in range(len(sorted_word), 0, -1):
        if not isFound:
            for substring_letters_list in itertools.combinations(sorted_word, i):
                substring_letters = "".join(substring_letters_list)
                # Checks the sorted letters with the small sorted dictionary and adds the found words to a list.
                if substring_letters in sorted_small_dictionary:
                    index = sorted_small_dictionary.index(substring_letters)
                    list_of_winning_words.append(small_dictionary[index])
                    isFound = True
        else:
            # Removing repeated words.
            list_of_winning_words = remove_repeats(list_of_winning_words)
            return list_of_winning_words


def ascii_text():
    """ Prints out an ASCII art to display 'Countdown'. """
    # ASCII art
    print('  _____                  _      _                       _ ')
    print(' / ____|                | |    | |                     | |')
    print('| |     ___  _   _ _ __ | |_ __| | _____      ___ __   | |')
    print('| |    / _ \\| | | | \'_ \\| __/ _` |/ _ \\ \\ /\\ / / \'_ \\  | |')
    print('| |___| (_) | |_| | | | | || (_| | (_) \\ V  V /| | | | |_|')
    print(' \\_____\\___/ \\__,_|_| |_|\\__\\__,_|\\___/ \\_/\\_/ |_| |_| (_)')
    print('\n')


def check_answer(letters, answer):
    """ Takes a random string of vowels and consonants called letters, also takes in the answer from the user. Checks
    if the characters from answer is contained in letters as well as check if its in the dictionary. Prints out the
    user's score if answer is right. """
    dictionary = dictionary_reader(DICTIONARY_FILE)
    score = str(len(answer))
    sorted_letter = ''.join(sorted(letters))
    sorted_answer = ''.join(sorted(answer))
    sorted_list_of_letters = []
    isCorrect = False
    # Creates a list of combinations of random letters.
    sorted_word = "".join(sorted(sorted_letter))
    for i in range(len(sorted_word), 0, -1):
        for substring_letters_list in itertools.combinations(sorted_word, i):
            substring_letters = "".join(substring_letters_list)
            sorted_list_of_letters.append(substring_letters)
    # Checking if sorted answer is in the combinations of random letters.
    for i in sorted_list_of_letters:
        if i == sorted_answer:
            isCorrect = True

    if isCorrect and (answer in dictionary):
        print("You scored " + score + " points!")
        # Return only for tests
        return True
    else:
        print('Invalid word or word not found in the dictionary!')
        # Return only for tests
        return False


def run_game():
    """ Runs the game logic. Runs functions from above. """
    ascii_text()
    letters = select_characters()
    player_input = input("You have 30 seconds to enter your word using " + "\'" + letters + "\':  ")
    print('\n')
    check_answer(letters, player_input)
    best_possible_answers = word_lookup(letters)
    print('\n')
    print("Longest possible words:")
    for i in best_possible_answers:
        print(i)


# TESTS
def tests():
    """ Tests for functions above. """
    number_of_tests_passed = 0
    # Tests for remove_repeats()
    test_list_a = ['a', 'b', 'c', 'd', 'c']
    if remove_repeats(test_list_a) == ['a', 'b', 'c', 'd']:
        number_of_tests_passed += 1

    # Tests for dictionary_reader()
    if dictionary_reader(DICTIONARY_FILE)[2] == 'aa':
        number_of_tests_passed += 1
    dictionary_len = len(dictionary_reader(DICTIONARY_FILE))
    if dictionary_reader(DICTIONARY_FILE)[dictionary_len - 2] == 'Zyzzogeton':
        number_of_tests_passed += 1
    if dictionary_reader(DICTIONARY_FILE)[dictionary_len - 1] == '':
        number_of_tests_passed += 1

    # Tests for word_lookup()
    test_letters_a = 'abcdefghi'
    if word_lookup(test_letters_a) == ['bighead']:
        number_of_tests_passed += 1
    test_letters_b = 'bob'
    if word_lookup(test_letters_b) == ['bob']:
        number_of_tests_passed += 1
    test_letters_c = 'a'
    if word_lookup(test_letters_c) != ['a']:
        number_of_tests_passed += 1

    # Tests for check_answer()
    if check_answer('equianglec', 'equiangle'):
        number_of_tests_passed += 1
    if not check_answer('equianglec', 'aquiangle'):
        number_of_tests_passed += 1
    if not check_answer('equianglec', 'bob'):
        number_of_tests_passed += 1

    number_of_tests_passed = str(number_of_tests_passed)
    print('Passed ' + number_of_tests_passed + ' out of 10 tests!')


if __name__ == '__main__':
    """ Run tests or game here. """
    # tests()
    run_game()
