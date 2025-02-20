import curses as cur
from curses import wrapper as wp

def wpm_test(stdscr):
  target_text = "Hello world, This is some text"
  current_text = []

  while True:
   
    stdscr.clear()
    display_text(stdscr,target_text,current_text)
     
    stdscr.refresh()
     
    key = stdscr.getkey() 
    if ord(key) == 27:
      break

    if key in ("KEY_BACKSPACE","\b","\x7f"):
       if len(current_text)>0:
         current_text.pop()
    else:
       current_text.append(key) 


def start_screen(stdscr):
 stdscr.clear()
 stdscr.addstr("Welcome to Speed Test!")
 stdscr.addstr("\n press any key to begin!")
 stdscr.refresh()

 stdscr.getkey() 


def display_text(stdscr,target,current,wpm = 0):
 stdscr.addstr(target)
 
 for i, char in enumerate(current):
  stdscr.addstr(0,i,char, cur.color_pair(1))


 


def main(stdscr):
  cur.init_pair(1,cur.COLOR_GREEN,cur.COLOR_WHITE)
  cur.init_pair(2,cur.COLOR_RED,cur.COLOR_WHITE)

  start_screen(stdscr)
  wpm_test(stdscr)

wp(main)

