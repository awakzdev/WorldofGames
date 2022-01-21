def difficulty():
    while True:
        try:
          input_diff = int(input("Pick a difficulty between 1-5: "))

        except ValueError:
            print("Please enter a number")

        if 1 <= input_diff < 6:
            break
        else:
            print("Enter a difficulty within the given range")

    print(f"Your difficulty is: {input_diff}")
    return input_diff
