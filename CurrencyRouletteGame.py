import random
import requests


def currency_roulette_game(diff):
    url = f'https://v6.exchangerate-api.com/v6/e01de27e3fb2e4ac40d77e31/pair/USD/ILS'

    response = requests.get(url)
    data = response.json()

    converted_number = data['conversion_rate']

    # converted_number will convert the rate of USD to ILS = 3.18
    # diff is equal to difficulty
    number_chosen = random.randint(0, 50)
    rate = (converted_number * number_chosen - (5 - diff), converted_number * number_chosen + (5 - diff))
    print(f"The number generated is: {number_chosen}")
    user_input = int(float(input("Convert the value of the number from USD to ILS: ")))

    min_range = rate[0]
    max_range = rate[1]

    if min_range < user_input < max_range:
        print("True")
        return True
    else:
        print("False")
        return False
