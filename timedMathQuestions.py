import random as r 

OPERATORS = ["+", "-","*","/"]
MIN_OPERAND = 3
MAX_OPERAND = 12

def generate_problem():
  left = r.randint(MIN_OPERAND,MAX_OPERAND)
  right = r.randint(MIN_OPERAND,MAX_OPERAND)
  operator = r.choice(OPERATORS)

  exp = str(left) + operator  + str(right)

  answer = eval(exp)
  return exp, answer


exp, answer = generate_problem()

print(exp, answer)