# This is a sample Python script.

# added auto format on save


def feet_to_steps(userInput):
    return round(userInput / 2.5)


if __name__ == '__main__':
    # Type your code here.
    while True:
        user_feet = float(input("Enter feet to convert to steps: "))
        print(feet_to_steps(user_feet))
        retry = input("Try again? (y/n) ")
        if retry.lower() == 'n':
            print("Good Bye")
            break

    print("This is something")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
