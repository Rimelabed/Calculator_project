
import re
def arithmetic_arranger(problems, solve= False):

    first = ""
    second = ""
    lines = ""
    sumx = ""
    string = ""
    if(len(problems)>5):
        return"Error"
    for problem in problems:

        if (re.search("[^\s0-9.+-]", problem)):

            if (re.search("[/]", problem) or re.search("[*]", problem)):
                return "Error"
            return "Error"

        firstNumber = problem.split(" ")[0]
        operator = problem.split(" ")[1]
        secondNumber = problem.split(" ")[2]
        if (len(firstNumber) >= 5 or len(secondNumber) >= 5):
            return "Error"

        sum = ""

        if (operator == "+"):
            sum = str(int(firstNumber) + int(secondNumber))
        elif (operator == "-"):
            sum = str(int(firstNumber) - int(secondNumber))

        length = max(len(firstNumber), len(secondNumber)) + 2
        top = str(firstNumber).rjust(length)
        bottom = operator + str(secondNumber).rjust(length-1)
        line = ""
        res = str(sum).rjust(length)
        for s in range(length):
            line += "-"
        if problem != problems[-1]:
            first += top + '  '
            second += bottom + '  '
            lines += line + '  '
            sumx += res + '  '
        else:
            first += top
            second += bottom
            lines += line
            sumx += res
    if solve:
        string = first + "\n" + second + "\n" + lines + "\n" + sumx
    else:
        string = first + "\n" + second + "\n" + lines
    return string












s=""
solve=True
problems=["578 + 234", "672 + 981"]
s=arithmetic_arranger(problems, solve)
print(s)










