import random as r 
import time as t

OPERATORS = ["+", "-","*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 2

def generate_problem():
  left = r.randint(MIN_OPERAND,MAX_OPERAND)
  right = r.randint(MIN_OPERAND,MAX_OPERAND)
  operator = r.choice(OPERATORS)

  exp = str(left) + operator  + str(right)

  answer = eval(exp)
  return exp, answer


wrong = 0
input("press enter to start")
print("__________________")

start_time = t.time()

for i in range(TOTAL_PROBLEMS):
 exp, answer = generate_problem()
 while True:
   guess = input("problem #" + str(i+1) + ":" + exp + "=" )
   if guess == str(answer):
     break
   wrong  += 1

    

print("____________________")
end_time = t.time()
total_time = round(end_time - start_time)
print(f'You completed the task in {total_time} secs')