import turtle as tur
import time as t
import random as r
WIDTH , HEIGHT  = 500 , 600
COLORS = ['red','green','blue', 'orange','yellow','black','purple','pink','brown','cyan']
 

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

def create_turtles(colors):
 turtles = []
 spacingx = WIDTH // (len(colors)+1)
 for i, color in enumerate(colors):
   racer = tur.Turtle()
   racer.color(color)
   racer.shape('turtle')
   racer.left(90)
   racer.penup() 
   racer.setpos(-WIDTH //2 + (i+1)* spacingx, -HEIGHT //2 +20 )
   racer.pendown()
   turtles.append(racer) 

 return turtles


def race(colors):
   turtles = create_turtles(colors)
   
   while True:
    for racer in turtles:
      distance  = r.randrange(1,20)
      racer.forward(distance)

      x,y  = racer.pos()
      if y >= HEIGHT // 2 -10:
        return colors[turtles.index(racer)]



racers = get_num_of_racers()
init_turtle()

r.shuffle(COLORS)
colors = COLORS[:racers]
winner  = race(colors)
print(winner)
















































# racer = tur.Turtle()
# racer.speed(1)
# racer.shape('turtle')
# racer.color('red')
# racer.penup()
# racer.forward(100)
# racer.left(90)
# racer.forward(100)
# racer.right(90)
# racer.backward(100)


