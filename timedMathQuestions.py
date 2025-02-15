import random as r 

OPERATORS = ["+", "-","*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 5
def generate_problem():
  left = r.randint(MIN_OPERAND,MAX_OPERAND)
  right = r.randint(MIN_OPERAND,MAX_OPERAND)
  operator = r.choice(OPERATORS)

  exp = str(left) + operator  + str(right)

  answer = eval(exp)
  return exp, answer




for i in range(TOTAL_PROBLEMS):
 exp, answer = generate_problem()
 while True:
   guess = input("problem #" + str(i+1) + ":" + exp + "=" )
   if guess == str(answer):
     break
