import random_word
import random

from random_word import RandomWords
def get_valid_words(words):
    r=RandomWords()
    word = r.get_random_word()
    while '_' in word or ' ' in word:
        word = random.choice(words)
    print(word)
get_valid_words()
