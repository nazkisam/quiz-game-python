SCORE_COUNT = 0

print("welcome to Quiz Game")
playing  = input("Press y to play / x to exit: ")
if playing  == 'x':
 quit()

print('lets play 😁')

answer = input("what is the full form of cpu").lower()
if answer == 'central processing unit':
 SCORE_COUNT += 1
 print(f'{answer} is correct answer. score  = {SCORE_COUNT}')

else:
 SCORE_COUNT -=1
 print(f'{answer} is wrong answer, correct answer is"central processing unit"  score = {SCORE_COUNT}')


answer = input("what does GPU stand for?").lower()
if answer == 'graphics process unit':
 SCORE_COUNT += 1
 print(f'{answer} is correct answer. score  = {SCORE_COUNT}')

else:
 SCORE_COUNT -=1
 print(f'{answer} is wrong answer, correct answer is"central processing unit"  score = {SCORE_COUNT}')

answer = input("what does RAM stand for").lower()
if answer == 'random access memory':
 SCORE_COUNT += 1
 print(f'{answer} is correct answer. score  = {SCORE_COUNT}')

else:
 SCORE_COUNT -=1
 print(f'{answer} is wrong answer, correct answer is"random access memory"  score = {SCORE_COUNT}')

print (f'{(SCORE_COUNT/3)*100}%')

 