import difficulty
import Utils
import os


def score_adder(diff):
    if not os.path.isfile(Utils.utils()):
        with open(Utils.utils(), 'a+') as file:
            file.write(str('0'))

    with open(Utils.utils(), 'r+') as file:
        current_score = int(file.read())
        file.seek(0)
        file.write(str(current_score + ((diff * 3) + 5)))
