# print("hello world")

# print("    /|")
# print("   / |")
# print("  /  |")
# print(" /___|")

# character_name = "Pratt"
# character_age = "23"
# age = 23
# is_male = False

# print("There once was a man named " + character_name + ", ")
# print("he was " + character_age + " years old.")
# print("he really liked the name " + character_name + ", ")
# print("but didn't like being " + character_age)

# phrase = "Giraffe Academy"
# print(len(phrase))
# print(phrase[0])
# print(phrase.index("c"))
# print(phrase.replace("Giraffe", "Elephant"))
# print(phrase)
# print(-2.75)
# print(3 + 5)
# print(3 * 4 + 5)
# print(10 % 3)

# my_num = -5
# print("I have " + str(my_num) + " kids")
# print(abs(my_num))
# print(pow(3,2))
# print(max(4,100))
# print(min(4,100))
# print(round(3.49))


from math import *

# print(floor(2.4))
# print(ceil(2.4))
# print(sqrt(36))

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello " + name + "! You are " + age)

# num1 = float(input("Enter a number: "))
# num2 = float(input("Enter another number: "))
# result = num1 + num2
# print(result)


# Mad LIBS Game
# color = input("Enter a color: ")
# plural_noun = input("Enter a plural noun: ")
# celebrity = input("Enter a celebrity: ")

# print("Roses are " + color)
# print(plural_noun + " are blue")
# print("I love " + celebrity)


# Lists
lucky_numbers = [4, 42, 2, 8, 15, 23, 1, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Jim", "Jim", "Oscar", "Toby"]
friends.append("Creed")
friends.insert(1, "Kelly")
# friends.remove("Jim")
friends.pop()
friends.sort()
lucky_numbers.sort()
lucky_numbers.reverse()

friends2 = friends.copy()

# Clears a list of everything
# friends.clear()

# friends.extend(lucky_numbers)

# print(friends)
# print(friends.index("Karen"))
# print(friends.count("Jim"))

# print(lucky_numbers)
# print(friends2)

# friends[1] = "Mike"
# print(friends)
# print(friends[2])
# print(friends[1:4])

# TUPLES (it's inmutable,can't change the values in a tuple after creating it)
coordinates = [(4, 5), (8, 5), (3, 4), (80, 25)]
print(coordinates[0])
print(coordinates[0][1])
