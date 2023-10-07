# Closure is a function having access to the scope of its parent
# function after the parent function has returned.


def parentFunctions(person):
    coins = 3

    def playGame():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        else:
            print("\n" + person + " is out of coins.")

    return playGame


arthur = parentFunctions("Arthur")
alliah = parentFunctions("Alliah")

arthur()
arthur()
arthur()
alliah()
alliah()
alliah()
