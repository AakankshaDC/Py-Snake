import curses
from random import randint

def init():
	# setup the window
	curses.initscr()
	window = curses.newwin(20,60,0,0) # x = 60 y = 20 starting coordiunate = 0,0
	window.keypad(1) # allow arrow keys to control our snakee
	curses.noecho() # dont want no other input to intrefere with our tereminal
	curses.curs_set(0) # hide cursor

	window.border(0)
	window.nodelay(1) # continue and dont wait for user to add input

	snake = [(4,10), (4,9), (4,8)]
	food = (10,20)

	return window, snake, food

def game_logic(window, snake, food):
	# window = init()
	window.addch(food[0],food[1],curses.ACS_PI)
	ESC = 27
	score = 0

	key = curses.KEY_RIGHT
	while key!= ESC:
		window.addstr(0,2,' Score: '+str(score)+ ' ')
		window.timeout(150-(len(snake)) // 5 + len(snake)//10 % 120) # increase speed based on the len of snake

		prev_key = key
		event = window.getch()
		key = event if event != -1 else prev_key

		if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, ESC]:
			key = prev_key

		# calc the next coordinates for snake
		cur_head_cord_y = snake[0][0]
		cur_head_cord_x = snake[0][1]

		if key == curses.KEY_DOWN: cur_head_cord_y += 1
		if key == curses.KEY_UP: cur_head_cord_y -= 1
		if key == curses.KEY_LEFT: cur_head_cord_x -= 1
		if key == curses.KEY_RIGHT: cur_head_cord_x += 1


		# update snake 
		snake.insert(0,(cur_head_cord_y, cur_head_cord_x))

		# check if we hit the corners
		if cur_head_cord_y == 0 or cur_head_cord_y == 19 : break
		if cur_head_cord_x == 0 or cur_head_cord_x == 59: break

		# if snake runs over itself
		if snake[0] in snake[1:]: break

		# if snake hit food
		if snake[0] == food:
			# eat food
			score += 1
			food = ()
			while food == ():
				food = (randint(1,18), randint(1,58))
				if food in snake:
					# we dont want to use this
					food = ()
			window.addch(food[0],food[1],curses.ACS_PI)
		else:
			# move snake, remove tail
			last_coord = snake.pop()
			window.addch(last_coord[0], last_coord[1], ' ')


		window.addch(snake[0][0],snake[0][1],'*')
		

	curses.endwin()
	print(f"Final Score: {score}")

win, snake, food = init()
game_logic(win, snake, food)
