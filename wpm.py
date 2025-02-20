import curses as cur
from curses import wrapper as wp
import time as t
import random as r


def load_text():
  with open("text.txt","r") as txt:
   lines = txt.readlines()
   return r.choice(lines).strip()




def wpm_test(stdscr):
  target_text = load_text()
  current_text = []

  wpm = 0
  start_time = t.time()
  stdscr.nodelay(True)


  while True:
    time_elapsed = max(t.time() - start_time,1)
    wpm = round((len(current_text) / (time_elapsed / 60))/5)

    stdscr.clear()
    display_text(stdscr,target_text,current_text,wpm)
     
    stdscr.refresh()

    if "".join(current_text) == target_text:
      stdscr.nodelay(False)
      break
    try: 
      key = stdscr.getkey() 
    except:
      continue


    if ord(key) == 27:
      break

    if key in ("KEY_BACKSPACE","\b","\x7f"):
       if len(current_text)>0:
         current_text.pop()
    elif len(current_text) < len(target_text):
       current_text.append(key) 











def start_screen(stdscr):
 stdscr.clear()
 stdscr.addstr("Welcome to Speed Test!")
 stdscr.addstr("\n press any key to begin!")
 stdscr.refresh()

 stdscr.getkey() 


def display_text(stdscr,target,current,wpm = 0):
 stdscr.addstr(target)
 stdscr.addstr(1,0,f"WPM:{wpm}")
 
 for i, char in enumerate(current):
  correct_char = target[i]
  color = cur.color_pair(1)
  if char != correct_char:
    color = cur.color_pair(2)
  stdscr.addstr(0,i,char, color )


 


def main(stdscr):
  cur.init_pair(1,cur.COLOR_GREEN,cur.COLOR_WHITE)
  cur.init_pair(2,cur.COLOR_RED,cur.COLOR_WHITE)

  start_screen(stdscr)
  while True:  
   wpm_test(stdscr)
   stdscr.addstr(2,0,"you completed the test, press any key to continue...")
   key = stdscr.getkey()
  
   if ord(key) == 27:
     break
   

wp(main)

