import random
import pandas as pd


class WordleGame:
    result = ['[B]', '[B]', '[B]', '[B]', '[B]']

    def __init__(self, _word_list, no_of_guesses):
        self._word_list = _word_list
        self._random_chosen_word = random.choice(_word_list)
        self._no_of_guesses = no_of_guesses
        
    def is_invalid_word(self, _user_guessed_word):
        if len(_user_guessed_word) != 5:
            print(f'Must be 5 letter word')
            return True
        elif _user_guessed_word not in self._word_list:
            print(f'Must be a valid word')
            return True
        return False

    def is_ended(self):
        return self._no_of_guesses == 0

    def remaining_tries(self):
        return self._no_of_guesses

    def match_word(self, _user_guessed_word):
        self._no_of_guesses -= 1
        if self._replace_colours(_user_guessed_word):
            print("you won the game", _user_guessed_word)
            return True
        else:
            print(list(zip(list(_user_guessed_word), wordle_game.result)))
            self.result = ['[B]', '[B]', '[B]', '[B]', '[B]']  # resetting
            return False

    def _replace_colours(self, _user_guessed_word):
        zipped_random_and_user_word = list(zip(self._random_chosen_word, _user_guessed_word))
        char_list_random_chosen_word = list(self._random_chosen_word)
        is_full_match = True
        for i in range(5):
            if zipped_random_and_user_word[i][0] == zipped_random_and_user_word[i][1]:
                self.result[i] = '[G]'
                char_list_random_chosen_word[i] = '*'  # Invalid char because already matched with position
            elif zipped_random_and_user_word[i][1] in char_list_random_chosen_word:
                self.result[i] = '[Y]'
                is_full_match = False
            else:
                is_full_match = False
        return is_full_match


def initiate_game():
    url = 'https://raw.githubusercontent.com/charlesreid1/five-letter-words/master/sgb-words.txt'
    df = pd.read_csv(url, names=['Words'])
    word_list = df['Words'].tolist()
    return WordleGame(word_list, 6)


if __name__ == '__main__':
    wordle_game = initiate_game()

    while True:
        if wordle_game.is_ended():
            print("you loose the game")
            break
        else:
            user_word = input(f'Enter 5 character word, {wordle_game.remaining_tries()} tried left: ').lower()
            if wordle_game.is_invalid_word(user_word):
                continue
            elif wordle_game.match_word(user_word):
                break