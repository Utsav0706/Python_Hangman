import random
import art, words

lives = 6

print(art.logo)

chosen_word = random.choice(words.word_list)
print(chosen_word)

placeHolder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeHolder += "_"

print("Word to guess: " + placeHolder)

