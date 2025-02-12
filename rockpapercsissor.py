import random as r




def gg():
 while True:
   user_input = input("choose 1:Rock,2:Paper,3:scissor,x:quit").lower()
   if user_input == '1' or user_input == 'Rock':
      user_input = 'rock'
   elif user_input == '2' or user_input == 'paper':
      user_input = 'paper'
   elif user_input == '3' or user_input == 'scissors':
      user_input = 'scissors'
   elif user_input == 'x':
    quit() 
   return user_input


def comp_inp():
    random_num = r.randint(0, 2)  # Generates a random number between 0 and 2
    comp = ''

    if random_num == 0:
        comp = 'rock'
    elif random_num == 1:
        comp = 'paper'
    elif random_num == 2:
        comp = 'scissors' 

    return comp 







def gp(user_input,comp):
 USER_WINS = 0
 COMP_WINS = 0
 if user_input == comp:
    print(f"your move:{user_input}, Machine's move:{comp} --> tie")
 elif user_input == 'rock' and comp == 'paper':
    print(f"your move:{user_input}, Machine's move:{comp} --> computer won")
    COMP_WINS += 1
 elif user_input == 'paper' and comp == 'rock':
    print(f"your move:{user_input}, Machine's move:{comp} --> you won")
    USER_WINS += 1
 elif user_input == 'rock' and comp == 'scissors':
    print(f"your move:{user_input}, Machine's move:{comp} --> you won")
    USER_WINS += 1
 elif user_input == 'scissors' and comp == 'rock':
    print(f"your move:{user_input}, Machine's move:{comp} --> you won")
    COMP_WINS += 1
 elif user_input == 'scissors' and comp == 'paper':
    print(f"your move:{user_input}, Machine's move:{comp} --> you won")
    USER_WINS += 1

 return COMP_WINS,USER_WINS  
 
while True:
 user_input = gg()
 comp_inpp = comp_inp()

 print(user_input)
 print(comp_inpp)

 result = gp(user_input,comp_inpp)
 print(result)




       