# COUNTDOWN #
import random
from itertools import combinations


def select_characters():
    random_string = []
    list_of_vowels = ['a', 'e', 'i', 'o', 'u']
    list_of_consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j',
                          'k', 'l', 'm', 'n', 'p', 'q', 'r',
                          's', 't', 'v', 'w', 'x', 'y', 'z']
    # Loop for taking in user input and giving out C and V.
    i = 0
    while i < 9:
        user_input = input('Enter c for a consonant and v for a vowel.')
        if user_input == 'c' or user_input == 'C':
            random_string.append(random.choice(list_of_consonants))
            i += 1
        elif user_input == 'v' or user_input == 'V':
            random_string.append(random.choice(list_of_vowels))
            i += 1
        else:
            pass
    # Joins the things in the list into a string.
    new_string = ''.join(map(str, random_string))
    return new_string


def dictionary_reader(file_name):
    list_of_words = []
    file_name = str(file_name)
    read_file = open(file_name, "r")
    for _ in read_file:
        list_of_words.append(read_file.readline())
    read_file.close()
    # Removing '/n' from the list of words.
    list_of_words = [sub[:-1] for sub in list_of_words]
    return list_of_words


def word_lookup(random_string):
    list_of_words = dictionary_reader('words.txt')

    test_letters = random_string
    # sort the letters
    sorted_word = "".join(sorted(test_letters))
    # starting with the longest letter string count down to zero
    for i in range(len(sorted_word), 0, -1):
        # for each length of letter strings generate all possible combinations
        for substring_letters_list in combinations(sorted_word, i):
            # for each combination of letters convert list to string
            substring_letters = "".join(substring_letters_list)
            # substring_letters should then be compared with a sorted_word_list
            # print(substring_letters)  # printing is only here for test purposes

    random_list = []
    for i in substring_letters:
        random_list.append(i)

    for item1 in list_of_words:
        for item2 in random_list:
            if item1 == item2:
                print(item1)
            else:
                # print('no match')
                pass


# TESTS
# print(select_characters())
# print(dictionary_reader('words.txt'))
# word_lookup('abcdef')

if __name__ == '__main__':
    random_letters = select_characters()
    word_lookup(random_letters)
    # print(random_letters)
