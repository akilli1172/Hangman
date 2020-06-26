
import random

kelimeler = ["azure", "blizzard", "crypt", "dwarves", "euouae", "frizzled", "gizmo", "haphazard", "jogging", "megahertz",
             "nightclub", "scratch", "strength", "wave", "wizard", "yummy", "zipper", "pixel", "kayak", "kilobyte",
             "croquet", "buffalo", "pajama", "rhythm", "yippee"]

secret_word =random.choice(kelimeler)
LettersList = []
_list = []
hak = len(secret_word) + 5
for k in secret_word:
    LettersList.append((k))
for l in range(0, len(secret_word)):
    _list.append('_')

letters_guessed = []
print("Welcome to the game Hangman! ")
print("I am thinking of a word that is {} letters long.".format(len(secret_word)))
print("You have {} guesses left.".format(hak))


def is_word_guessed(secret_word, letters_guessed):
    global tahmin
    global hak
    tahmin = input("Please guess a letter:")
    if tahmin in letters_guessed:
        print("Oops! You've already guessed that letter.")
        hak -= 1
        print("You have {} guesses left.".format(hak))
        return False

    elif tahmin in secret_word:
        letters_guessed.append(tahmin)
        ind = secret_word.index((tahmin))
        _list[ind] = tahmin
        hak -= 1

        return True
    elif tahmin not in secret_word:
        print("Wrong guess")
        letters_guessed.append(tahmin)
        hak -= 1
        print("You have {} guesses left.".format(hak))
        return False
    # return tahmin


def get_guessed_word(secret_word, letters_guessed):
    for j in LettersList:
        if j == tahmin:
            if LettersList.count(tahmin) > 1:
                g = LettersList.index(j)
                _list[g] = j
                LettersList[g] = " "
            else:
                g = LettersList.index(j)
                _list[g] = j
                LettersList[g] = " "
                print("Good guess: ", ' '.join([str(elem) for elem in _list]))
                if _list.count('_') == 0:
                    break;
                print("You have {} guesses left.".format(hak))


def get_available_letters(letters_guessed):
    letters = "abcdefghijklmnopqrstuvwxyz"
    for i in range(0, len(letters_guessed)):
        letters = letters.replace(letters_guessed[i], "")
    return letters


def play():
    while hak >= 1:
        if is_word_guessed(secret_word, letters_guessed) == True:
            get_guessed_word(secret_word, letters_guessed)
        if _list.count('_') == 0:
            print("\nCongratulations, you won! ")
            break;
        if hak < 1 and _list.count('_') != 0:
            print("You have ran out ouf guesses. The word was '{}'. YOU LOST".format(secret_word))
            break;
        print(get_available_letters(letters_guessed))


play()
