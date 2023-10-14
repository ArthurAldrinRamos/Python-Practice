person = "Arthur"
coins = 4


def templateValue(val1, val2):
    return "\n%s has %s coins left." % (val1, val2)


print("\n" + person + " has " + str(coins) + " coins left.")

message = "\n%s has %s coins left." % (person, coins)
print(message)

print(templateValue(person, coins))

message = "\n{} has {} coins left.".format(person, coins)
print(message)

message = "\n{1} has {0} coins left.".format(coins, person)  # Flipped
print(message)

message = "\n{person} has {coins} coins left.".format(person=person, coins=coins)
print(message)

player = {"person": "Arthur", "coins": 4}

message = "\n{person} has {coins} coins left.".format(**player)
print(message)

#########################################################
#####  f-Strings! This is definitely the way!!!!!!  #####
#########################################################

message = f"\n{person} has {coins} coins left."
print(message)

message = f"\n{person.lower()} has {coins} coins left."
print(message)

message = f"\n{player['person']} has {int(16 / 4)} coins left."
print(message)

#########################################################
###########  You can pass Formatting Options  ###########
#########################################################

num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}")

for num in range(1, 11):
    print(f"2.25 times {num} is {2.25 * num:.2f}")

print("\n")

for num in range(1, 11):
    print(f"{num} divided by 4.44 is {num / 4.44:.2f}")
