arranged_problems = []


def arithmetic_arranger(numbers, showAnswers=False):
    for number in numbers:
        if number.__contains__("+"):
            posNums = number.split("+")
            num1 = posNums[0].strip()
            num2 = posNums[1].strip()
            # =================================================================
            if len(num1) == 4 or len(num2) == 4:
                if showAnswers == True:
                    answer = str(int(num1) + int(num2)).rjust(6)
                else:
                    answer = ""

                sum = (
                    num1.rjust(6)
                    + "\n"
                    + "+".ljust(1)
                    + num2.rjust(5, " ")
                    + "\n"
                    + "----".center(6, "-")
                    + "\n"
                    + answer
                    + "\n"
                )

                arranged_problems.append(sum)
            # =================================================================
            elif len(num1) == 3 or len(num2) == 3:
                if showAnswers == True:
                    answer = str(int(num1) + int(num2)).rjust(5)
                else:
                    answer = ""

                sum = (
                    num1.rjust(5)
                    + "\n"
                    + "+".ljust(1)
                    + num2.rjust(4, " ")
                    + "\n"
                    + "----".center(5, "-")
                    + "\n"
                    + answer
                    + "\n"
                )

                arranged_problems.append(sum)
            # =================================================================
            else:
                if showAnswers == True:
                    answer = str(int(num1) + int(num2)).rjust(4)
                else:
                    answer = ""

                sum = (
                    num1.rjust(4)
                    + "\n"
                    + "+".ljust(1)
                    + num2.rjust(3, " ")
                    + "\n"
                    + "----".center(4, "-")
                    + "\n"
                    + answer
                    + "\n"
                )

                arranged_problems.append(sum)

        if number.__contains__("-"):
            posNums = number.split("-")
            num1 = posNums[0].strip()
            num2 = posNums[1].strip()
            # =================================================================
            if len(num1) == 4 or len(num2) == 4:
                if showAnswers == True:
                    answer = str(int(num1) - int(num2)).rjust(6)
                else:
                    answer = ""

                difference = (
                    num1.rjust(6)
                    + "\n"
                    + "-".ljust(1)
                    + num2.rjust(5, " ")
                    + "\n"
                    + "----".center(6, "-")
                    + "\n"
                    + answer
                    + "\n"
                )

                arranged_problems.append(difference)

            # =================================================================
            elif len(num1) == 3 or len(num2) == 3:
                if showAnswers == True:
                    answer = str(int(num1) - int(num2)).rjust(5)
                else:
                    answer = ""

                difference = (
                    num1.rjust(5)
                    + "\n"
                    + "-".ljust(1)
                    + num2.rjust(4, " ")
                    + "\n"
                    + "----".center(5, "-")
                    + "\n"
                    + answer
                    + "\n"
                )

                arranged_problems.append(difference)
            # =================================================================
            else:
                if showAnswers == True:
                    answer = str(int(num1) - int(num2)).rjust(4)
                else:
                    answer = ""

                difference = (
                    num1.rjust(4)
                    + "\n"
                    + "-".ljust(1)
                    + num2.rjust(3, " ")
                    + "\n"
                    + "----".center(4, "-")
                    + "\n"
                    + answer
                    + "\n"
                )

                arranged_problems.append(difference)

    # firstLine = arranged_problems[0]
    # secondLine = arranged_problems[1]
    # thirdLine = arranged_problems[2]
    # fourthLine = arranged_problems[3]

    return arranged_problems


arithmetic_arranger(["3133 - 32", "693 + 3", "26 - 4", "4 - 4"], True)
print(arranged_problems[0])
print(arranged_problems[1])
print(arranged_problems[2])
print(arranged_problems[3])


# else:
#                 print(num1.rjust(4))
#                 print("-".ljust(1) + num2.rjust(3, " "))
#                 print("----".center(4, "-"))
#                 if showAnswers == True:
#                     print(str(int(num1) - int(num2)).rjust(4))
