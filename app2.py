# Functions

def say_hi(name, age):
    print('Hello ' + name + ", you are " + str(age))


# say_hi("Mike", 20)
# say_hi("Pratt", 23)

# Return statement

def cube(num):
    return num*num*num

result = cube(4)
# print(result)

# IF CONDITION
is_male = True
is_tall = False

if is_male and is_tall:
    print('You are a tall male')
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print('You are not a male and not tall')
