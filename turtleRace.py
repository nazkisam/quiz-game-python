import turtle as tur


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


















print(get_num_of_racers())


