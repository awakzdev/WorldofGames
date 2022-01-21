import os


def utils():
    SCORES_FILE_NAME = "Scores.txt"
    global BAD_RETURN_CODE
    return SCORES_FILE_NAME


def screen_clean():
    x = input("to clean screen type, 'refresh' : ")
    if x == "refresh":
        os.system('clear'), os.system('clr')
    else:
        print("your input was incorrect, type 'refresh' correctly")
    return screen_clean()





