import random as r

def roll():
  min_value = 1
  max_value = 6
  roll = r.randint(min_value,max_value)

  return roll

value = roll()
print(value)
 

while True:
  players = input('Enter the number of players (2-4)')
  if players.isdigit():
     players = int(players)
     if 2 <= players <= 4:
      break
     
     else:
      print('must be between 2 - 4 players:') 
  else:
    print('Invalid,try again')    

print(players)

MAX_SCORE = 50

player_scores = [0 for _ in range(players)]
print(player_scores)

while max(player_scores) < MAX_SCORE:
 for player_idx in range(players):
  print('\nplayer number', player_idx +1 , 'turn has just started!\n')
  current_score = 0
 while True: 
  should_roll = input("enter y to roll")
  if should_roll != 'y':
    break
  value = roll()
  if value == 1:
   current_score = 0
   print('you rolled 1, turn done')
   break
  else:
    current_score += value
    print('you rolled a ',value)
  print('your score is',current_score)
 player_scores[player_idx] += current_score
 print('your total score is:',player_scores[player_idx])
