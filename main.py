import itertools
import string
import time


def guess_common_words(word):
    with open('words.txt', 'r') as words:
        data = words.read().splitlines()

    for i, match in enumerate(data):
        if match == word:
            return f'the word {match} was found on attempt no:{i}'
    return 0


def brute_force(word, min_password_lenght=4, max_password_lenght=10, digits=False, symbols=False,
                uppercase=False):
    chars = string.ascii_lowercase
    if digits:
        char = string.digits + string.ascii_lowercase
    if symbols:
        char = string.punctuation + string.ascii_lowercase
    if uppercase:
        char = string.ascii_uppercase + string.ascii_lowercase

    attempts = 0
    for word_lenght in range(min_password_lenght, max_password_lenght):
        for guess in itertools.product(chars, repeat=word_lenght):
            attempts += 1
            guess = ''.join(guess)
            if guess == word:
                number_of_attempts = '{:,}'.format(attempts)
                print(attempts)
                print(number_of_attempts)
                return f'\'{word}\' was found in {number_of_attempts} guesses'


search_term = input('enter your password: ').lower()
start_time = time.time()
common_search = guess_common_words(search_term)
print('Searching...')
if common_search != 0:
    print(common_search)
else:
    request = brute_force(search_term, min_password_lenght=3, max_password_lenght=10)
    print(request)
print(round(time.time() - start_time, 2), 's')
