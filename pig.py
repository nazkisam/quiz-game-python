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

#1:45:15

