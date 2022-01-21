import random
import requests


def currency_roulette_game(diff):
    url = f'https://v6.exchangerate-api.com/v6/e01de27e3fb2e4ac40d77e31/pair/USD/ILS'

    response = requests.get(url)
    data = response.json()

    y = data['conversion_rate']

    # Y will convert the rate of USD to ILS = 3.18
    # diff is equal to difficulty
    l = random.randint(0, 50)
    g = (y * l - (5 - diff), y * l + (5 - diff))
    print(f"The number generated is: {l}")
    z = int(float(input("Convert the value of the number from USD to ILS: ")))

    min_range = g[0]
    max_range = g[1]

    if min_range < z < max_range:
        print("True")
        return True
    else:
        print("False")
        return False
