import string


def high(x):
    i = 1
    o = 0
    z = 0
    alphaDict = {}
    splitX = x.split(" ")
    splitY = []

    for a in string.ascii_lowercase:
        alphaDict[a] = i
        i += 1
    # print(alphaDict)
    # print(splitX)

    for k in splitX:
        splitY.append(list(k))
        print(splitY[o])
        o += 1
    lmao = list("man i need a taxi up to ubud")


print(splitY)


high("man i need a taxi up to ubud")
