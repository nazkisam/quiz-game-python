import random as r


range_cap = input("input the top range of the number")

if  range_cap.isdigit():
    range_cap = int(range_cap)
    if range_cap < 0:
        print('enter a number greater than 0')
        quit()
else:
    print('Enter a number')
    quit()


random_number = r.randint(0,range_cap)
print(random_number)


guesses = 0
while True:
  guesses += 1
  user_guess = int(input("enter the number"))
  if user_guess ==random_number:
   print('correct guess') 
   break

  elif user_guess > random_number:
     print('you were above the number')
     if guesses < 3:
      continue
     else:
        print('wrong answer, guess again')
        break
  elif user_guess <  random_number:
     print("you were below the number")
     if guesses < 3:
      continue
     else:
        print('wrong answer, guess again')
        break
 
  
  
