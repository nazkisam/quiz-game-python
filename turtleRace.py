import turtle as tur
import time
WIDTH , HEIGHT  = 500 , 600


def get_num_of_racers():
  racers = 0
  while True:
    racers = input("enter the number of turtles from (2-10): ")
    
    if racers.isdigit():
     racers = int(racers)
     
     
    else:
     print('wrong input, should be digit')
     continue

    if 2<= racers <=10: 
      return racers

    else:
      print('wrong input, not in range')


def init_turtle():
  screen = tur.Screen()
  screen.setup(WIDTH,HEIGHT)
  screen.title('Turtle Game')

racers = get_num_of_racers()
init_turtle()

racer = tur.Turtle()
racer.forward(100)
racer.left(90)
racer.forward(100)
racer.right(90)
racer.backward(100)
time.sleep(10)

