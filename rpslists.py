import random as r

user_score = 0
computer_score = 0


options = ['rock','paper','scissors']
while True:
  user_input = input('enter rock/paper/scissors or x to quit')
  if user_input == 'x':
    break
  if user_input not in options:
    continue
  random_number = r.randint(0,2)
  computer_move = options[random_number] 
  print(f'computer_move:{computer_move}')

  if user_input == computer_move:
    print('tie')
  elif user_input == 'rock' and computer_move == 'scissors':
   print('you won')
  elif user_input == 'paper' and computer_move == 'rock':
    print('you won')
  elif user_input == 'scissor' and computer_move == 'paper':
    print('you won')
  else:
    print('you lost')     
  
