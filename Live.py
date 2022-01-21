import GuessGame
import MemoryGame
import CurrencyRouletteGame
import difficulty
import Score


def validate_number(top_value, msg):
    x = "0"
    while not (x.isdigit() and (1 <= int(x) <= top_value)):
        x = input(f"{msg} (1,{top_value}): ")

        if not x.isdigit():
            print(f"Selection needs to be a number (1 - {top_value})")
        elif int(x) < 1 or int(x) > top_value:
            print(f"Selection needs to be 1 - {top_value}")

    return int(x)


def load_game():
    while True:
        ismyscore = None
        my_selection = validate_number(3,
                                       "Please choose the game to play \n 1 - Memory Game - a sequence of numbers "
                                       "will appear "
                                       "for 1 second and you have to guess it back "
                                       "\n 2 - Guess Game - guess a number and see if you chose like the computer \n "
                                       "3 - "
                                       "Currency Roulette - try and guess the value of a random amount of USD in ILS")
        print(f"You have selected game number: {my_selection}")
        diff = difficulty.difficulty()

        if my_selection == 1:
            ismyscore = MemoryGame.memory_game(diff)
        if my_selection == 2:
            ismyscore = GuessGame.guess_game(diff)
        if my_selection == 3:
            ismyscore = CurrencyRouletteGame.currency_roulette_game(diff)

        if ismyscore:
            Score.score_adder(diff)


if __name__ == "__main__":
    load_game()
