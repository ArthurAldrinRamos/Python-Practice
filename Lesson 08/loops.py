# Loops

# value = 1
# while value <= 10:
#     print(value)
#     value += 1

print("")

names = ["Arthur", "Aldrin", "Ramos"]
actions = ["codes", "eats", "sleeps"]

for name in names:
    for action in actions:
        print(name + " " + action + ".")

# for x in names:
#     print(x)

# for x in names:
#     if x == "Aldrin":
#         break
#     print(x)

# for x in names:
#     if x == "Aldrin":
#         continue
#     print(x)

# for x in range(4):
#     print(x)
index = 0
for x in range(0, 1800, 100):
    index += 1
    print(x)
else:
    print("Good thing that's over!")


def move_zeros(lst):
    i = 0
    for x in lst:
        if x == 0:
            lst.remove(0)
            lst.append(0)

        i += 1
        print(x)

    return lst


print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))
print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
