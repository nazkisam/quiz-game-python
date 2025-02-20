import curses as cur
from curses import wrapper as wp


def start_screen(stdscr):
 stdscr.clear()
 stdscr.addstr(0,0,"\nWelcome to Speed Test!")
 stdscr.refresh()






def main(stdscr):
  cur.init_pair(1,cur.COLOR_GREEN,cur.COLOR_WHITE)
  cur.init_pair(2,cur.COLOR_RED,cur.COLOR_WHITE)
  stdscr.clear()
  stdscr.addstr(1,10,"Hello World!",cur.color_pair(2))
  stdscr.addstr(1,10,"Hello World!",cur.color_pair(2))
  stdscr.refresh()
  key  = stdscr.getkey()
  print(key)

wp(main)

