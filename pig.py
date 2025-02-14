import random as r

def roll():
  min_value = 1
  max_value = 6
  roll = r.randint(min_value,max_value)

  return roll

value = roll()
print(value)

