def hello_world():
    print("Hello World!")


hello_world()


def sum(num1=0, num2=0):
    if type(num1) is not int and type(num2) is not int:
        return "Please input a Number in both num1 and num2"
    elif type(num1) is not int:
        return "Please input a Number in num1"
    elif type(num2) is not int:
        return "Please input a Number in num2"
    return "The sum of " + str(num1) + " and " + str(num2) + " is " + str(num1 + num2)


total = sum("a", "b")
print(total)

total = sum(1, "b")
print(total)

total = sum("a", 1)
print(total)

total = sum(6, 4)
print(total)


def multiple_items(*args):
    print(args)
    print(type(args))


multiple_items(1, 2, 3)


def multi_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


multi_named_items(one=1, two=2, three=3)
