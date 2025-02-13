
name = input('enter your name')
print(f'Welcome, {name} to this adventure')

answer = input('you are on a dirt road,it has come to an end and you can go left or right, which way would you like to go').lower()

if answer == 'left':
  answer = input('you reached to a river,input walk to walk and swim to swim')
  if answer  == 'swim':
    print('you swam across, got eaten by an aligator 😂😂')
  elif answer == 'walk':
    print('you walked for many miles, ran out of wanter and died,😁😂')

elif answer == 'right':
   answer = input('you came to a bridge, it looks wobbly, enter back to go back, cross to cross')
   if answer  == 'back':
    print('you went back to main road 😑')
   elif answer == 'cross':
       answer = input('you crossed the bridge and met a stranger,would you like to talk (yes/no)')
       if answer == 'yes':
         print('you won ✨🎉🍕')
       elif answer == 'no':
        print('you lose')
     


