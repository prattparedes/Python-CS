# calculator
# num1 = float(input("Enter first number: "))
# op = input("Enter operator: ")
# num2 = float(input("Enter second number: "))

# if op == "+":
#     print(num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# elif op == "/":
#     print(num1 / num2)
# elif op == "*":
#     print(num1 * num2)
# else:
#     print("Invalid operator")

# Dictionaries
monthConversions = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

# print(monthConversions["Nov"])
# print(monthConversions.get("Dxc", "Not a valid Key"))
# print(monthConversions.get(0, "Not a valid Key"))
# print(monthConversions.get(3, "Not a valid Key"))

# While loop
# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# print('Done with loop')

# Guessing word game
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

# while guess != secret_word and not(out_of_guesses):
#     if guess_count < guess_limit:
#         guess = input("Enter guess: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True

# if out_of_guesses:
#     print("Out of Guesses, YOU LOSE!")
# else:
#     print("You win!")


# For Loop
# for letter in "Giraffe Academy":
#     print(letter)

# friends = ["Jim", "Karen", "Kevin"]
# for name in friends:
#     print(name)

# #range(3,10)
# for index in range(5):
#     print(index)
# for index in range(3, 10):
#     print(index)

# for index in range(len(friends)):
#     print(friends[index])

# for index in range(5):
#     if index == 0:
#         print('first iteration')
#     else:
#         print('Not first')

# Exponent functions
# def raise_to_power(base_num, pow_num):
#     result = 1
#     for index in range(pow_num):
#         result = result * base_num
#     return result

# print(raise_to_power(3, 4))

# 2D Lists and nested loops
number_grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0]]

# print(number_grid[2][2])
# for row in number_grid:
#     for col in row:
#         print(col)

# Build a translator
# Giraffe Language
# vowels -> g


def translate(phrase):
    translation = ""

    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation


# print(translate(input("Enter a phrase: ")))

# Try / Except


try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
    print("Divided by zero")
except ValueError:
    print("Invalid input")