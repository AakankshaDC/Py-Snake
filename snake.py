import curses

def init():
# setup the window
	curses.initscr()
	window = curses.newwin(20,60,0,0) # x = 60 y = 20 starting coordiunate = 0,0
	window.keypad(1) # allow arrow keys to control our snakee
	curses.noecho() # dont want no other input to intrefere with our tereminal
	curses.curs_set(0) # hide cursor

	window.border(0)
	window.nodelay(1) # continue and dont wait for user to add input

	return window

def game_logic(window):
# window = init()
	score = 0
	while True:
		event = window.getch()
	# ...

	curses.endwin()
	print(f"Final Score: {score}")

win = init()
game_logic(win)