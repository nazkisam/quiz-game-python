from playsound import playsound as ps
import time as t

CLEAR  = "\033[2J"
CLEAR_AND_RETURN = "\033[H"
 
def alarm(seconds):
  time_elapsed = 0
  print(CLEAR) 
  while time_elapsed < seconds:
    t.sleep(1)
    time_elapsed +=1
    time_left = seconds - time_elapsed
    minutes_left = time_left // 60 
    seconds_left = time_left % 60

    print(f'{CLEAR_AND_RETURN}time left: {minutes_left:02d}:{seconds_left:02d}')

    if minutes_left == 0 and seconds_left == 0: 
       ps("squid_game_new.mp3")




minutes = int(input('enter the number of minutes'))
seconds = int(input('enter the number of seconds'))
total_time_in_seconds = minutes * 60 +seconds

alarm(total_time_in_seconds)