import random
import string


def generate_password(length):
    lowercasealphabets = list(string.ascii_lowercase)
    uppercasealphabets = list(string.ascii_uppercase)
    numbers = list(range(9))
    password = []
    choices = ["lowercasestrings", "uppercasestrings", "numbers"]
    for i in range(length):
        choice = random.choice(choices)
        if choice == "lowercasestrings":
            alpha1 = random.choice(lowercasealphabets)
            password.append(alpha1)
        elif choice == "uppercasestrings":
            alpha2 = random.choice(uppercasealphabets)
            password.append(alpha2)
        elif choice == "numbers":
            num = random.choice(numbers)
            password.append(num)
    return ''.join(str(v) for v in password)


if __name__ == "__main__":
    get_length = int(input("enter the length: "))
    print(generate_password(length=get_length))
