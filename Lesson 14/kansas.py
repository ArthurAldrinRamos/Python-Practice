from random import choice

capital = "Topeka"
bird = "Western Meadowlark"
flower = "Sunflower"
song = "Home on the Range"


def randomFunFact():
    funFacts = [
        "Lorem Ipsum[0]",
        "Lorem Ipsum[1]",
        "Lorem Ipsum[2]",
        "Lorem Ipsum[3]",
        "Lorem Ipsum[4]",
    ]

    index = choice("01234")

    print(funFacts[int(index)])


if __name__ == "__main__":
    randomFunFact()
