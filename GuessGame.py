import random


def guess_game(diff):
    number = random.randint(1, diff * 2)
    if diff in range(1, 6):
        with open("secret_number.txt", 'w+') as my_file:
            my_file.writelines(f"{number}")
            my_file.close()
            print("Your number has been saved to a secret file.")
    else:
        print("Please enter a valid value.")

    game2(diff)


def game2(diff):
    x = 0
    if diff == 1:
        x = input("Guess a number between 1 to 2: ")
    elif diff == 2:
        x = input("Guess a number between 1 to 4: ")
    elif diff == 3:
        x = input("Guess a number between 1 to 6: ")
    elif diff == 4:
        x = input("Guess a number between 1 to 8: ")
    elif diff == 5:
        x = input("Guess a number between 1 to 10: ")
        print(x)

    my_files = open("secret_number.txt", 'r')
    content = my_files.read()
    print(content)

    if x == content:
        print("True")
        return True
    else:
        print("False")
        return False
