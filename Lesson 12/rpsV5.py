import sys
import random

# from enum import Enum

# class RPS(Enum):
#     ROCK = 1
#     PAPER = 2
#     SCISSORS = 3


def rps():
    gameCount = 0
    playerWins = 0
    pythonWins = 0

    def playRps():
        nonlocal playerWins
        nonlocal pythonWins

        template = "choose".upper().center(20, "=")
        choice_1 = "(1)".ljust(14, ".") + "ROCK🪨"
        choice_2 = "(2)".ljust(13, ".") + "PAPER📃"
        choice_3 = "(3)".ljust(10, ".") + "SCISSORS✂️"

        print(template)
        print(choice_1)
        print(choice_2)
        print(choice_3)
        print(template.casefold().replace("choose", "======"))

        playerChoice = input("👨 Your Pick: ")
        player = int(playerChoice)

        if playerChoice not in ["1", "2", "3"]:
            print("Please choose from 1, 2, or 3!")
            return playRps()

        if player == 1:
            rpsChoicePx = "ROCK 🪨"
        elif player == 2:
            rpsChoicePx = "PAPER 📃"
        elif player == 3:
            rpsChoicePx = "SCISSORS ✂️"

        computerChoice = random.choice("123")
        print("🤖 Python's Pick: " + computerChoice)
        print(template.casefold().replace("choose", "======"))
        computer = int(computerChoice)

        if computer == 1:
            rpsChoicePy = "ROCK 🪨"
        elif computer == 2:
            rpsChoicePy = "PAPER 📃"
        elif computer == 3:
            rpsChoicePy = "SCISSORS ✂️"

        print(rpsChoicePx.center(20, " "))
        print(" <> VS <> ".center(20, "="))
        print(rpsChoicePy.center(20, " "))
        print(template.casefold().replace("choose", "======"))

        def decideWinner(player, computer):
            nonlocal playerWins
            nonlocal pythonWins

            if player == 1 and computer == 3:
                playerWins += 1
                return "Player Won! 😃".center(20, " ")
            elif player == 2 and computer == 1:
                playerWins += 1
                return "Player Won! 😃".center(20, " ")
            elif player == 3 and computer == 2:
                playerWins += 1
                return "Player Won! 😃".center(20, " ")
            elif player == computer:
                return "It's a Tie!!!".center(20, " ")
            else:
                pythonWins += 1
                return "Python Won! 💔".center(20, " ")

        gameResult = decideWinner(player, computer)

        nonlocal gameCount
        gameCount += 1

        print("Game Count: " + str(gameCount))
        print("Player Wins: " + str(playerWins))
        print("Python Wins: " + str(pythonWins))

        print(gameResult)

        print("\nPlay Again?")

        while True:
            playAgain = input("\n 🥺 Play Again? \n    Y for Yes \n    Q to Quit\n")
            if playAgain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playAgain.lower() == "y":
            return playRps()
        else:
            print("Thank You for playing! 😃")
            sys.exit("Bye! 🙋‍♂️")

    return playRps


play = rps()

play()
