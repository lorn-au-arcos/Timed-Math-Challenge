import random
import time


OPERATOR = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10


def generateProblems():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATOR)

    calculation = str(left) + " " + operator + " " + str(right)
    answer = eval(calculation)
    return calculation, answer


wrong = 0
input("Press any key to start!")
print("------------------------------------")

start_time = time.time()


for i in range(TOTAL_PROBLEMS):
    calculation, answer = generateProblems()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + calculation + " =")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()

total_time = round(end_time - start_time, 2)

print("------------------------------------")
print("Well done! You did it in",  total_time, "seconds!")
