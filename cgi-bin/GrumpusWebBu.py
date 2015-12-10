#!/usr/bin/env python3

# David and Sam
# Hunt the Grumpus (Web Version)
# Dr. Warn's examples were very helpful especially 2-sequence.py

# initialization
import random

num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
	   11, 12, 13, 14, 15, 16, 17, 18, 19]
random.shuffle(num)
maze = [
		[num[0],[num[4],num[5],num[1]]],
	    [num[1],[num[0],num[7],num[2]]],
	    [num[2],[num[1],num[9],num[3]]],
	    [num[3],[num[2],num[11],num[4]]],
	    [num[4],[num[3],num[13],num[0]]],
	    [num[5],[num[0],num[6],num[14]]],
	    [num[6],[num[5],num[7],num[16]]],
	    [num[7],[num[1],num[8],num[6]]],
	    [num[8],[num[7],num[9],num[17]]],
	    [num[9],[num[2],num[10],num[8]]],
	    [num[10],[num[9],num[11],num[18]]],
	    [num[11],[num[3],num[12],num[10]]],
	    [num[12],[num[11],num[13],num[19]]],
	    [num[13],[num[4],num[14],num[12]]],
	    [num[14],[num[13],num[5],num[15]]],
	    [num[15],[num[14],num[16],num[19]]],
	    [num[16],[num[6],num[15],num[17]]],
	    [num[17],[num[16],num[18],num[8]]],
	    [num[18],[num[10],num[17],num[19]]],
	    [num[19],[num[18],num[15],num[12]]],
	   ]

# load cookie
import http.cookies
import os

cave1, cave2, bat1, bat2, pos, grump = random.sample(num, 6)
first_run = 0

cookie = http.cookies.SimpleCookie()
cookie_string = os.environ.get('HTTP_COOKIE')
if cookie_string == '':
    cookie_output = "I don't see a cookie."
else:
    cookie.load(cookie_string)
    first_run = cookie['first_run'].value
    if (first_run == 0):
        first_run = 1
    else:
        pos = int(cookie['pos'].value)
        grump = int(cookie['grump'].value)
        cave1 = int(cookie['cave1'].value)
        cave2 = int(cookie['cave2'].value)
        bat1 = int(cookie['bat1'].value)
        bat2 = int(cookie['bat2'].value)
        maze[0] = eval(cookie['maze0'].value)
        maze[1] = eval(cookie['maze1'].value)
        maze[2] = eval(cookie['maze2'].value)
        maze[3] = eval(cookie['maze3'].value)
        maze[4] = eval(cookie['maze4'].value)
        maze[5] = eval(cookie['maze5'].value)
        maze[6] = eval(cookie['maze6'].value)
        maze[7] = eval(cookie['maze7'].value)
        maze[8] = eval(cookie['maze8'].value)
        maze[9] = eval(cookie['maze9'].value)
        maze[10] = eval(cookie['maze10'].value)
        maze[11] = eval(cookie['maze11'].value)
        maze[12] = eval(cookie['maze12'].value)
        maze[13] = eval(cookie['maze13'].value)
        maze[14] = eval(cookie['maze14'].value)
        maze[15] = eval(cookie['maze15'].value)
        maze[16] = eval(cookie['maze16'].value)
        maze[17] = eval(cookie['maze17'].value)
        maze[18] = eval(cookie['maze18'].value)
        maze[19] = eval(cookie['maze19'].value)

caves = [
		  cave1, cave2
		]
bats = [
		  bat1, bat2
	   ]

alive = True
dead = False

# form information
import cgi
form = cgi.FieldStorage()

home_form = """
    <form method="get" action="/cgi-bin/GrumpusWeb.py">
        What you wanna do (move/shoot): <input type="text" name="home">
        <input type="submit" value="Submit">
    </form>
"""

move_form = """
   <form method="get" action="/cgi-bin/GrumpusWeb.py">
        Go to: <input type="text" name="move">
        <input type="hidden" name="home" value="__HOME__">
        <input type="submit" value="Submit">
    </form> 
"""

shoot_form = """
   <form method="get" action="/cgi-bin/GrumpusWeb.py">
        Where you shootin: <input type="text" name="shoot">
        <input type="hidden" name="home" value="__HOME__">
        <input type="submit" value="Submit">
    </form>
"""

home = form.getvalue('home')

# form logic
if 'home' not in form or home == '':
    form_output = home_form
    if 'move' in form:
        newpos = int(form.getvalue('move'))
        move = ''

        test = 0
        i = 0
        while i < 3:
            if maze[pos][1][i] == newpos:
                test += 1
            i += 1

            if test > 0:
                x = 0
                while x < 20:
                    if maze[x][0] == newpos:
                        pos = x
                        break
                    x += 1
        
    shoot = ''
elif home == 'move':
    if 'move' not in form or move == '':
        home = ''
        form_output = move_form.replace('__HOME__', home)
elif home == 'shoot':
    if 'shoot' not in form or shoot == '':
        home = ''
        form_output = shoot_form.replace('__HOME__', home)
else:
    form_output = home_form.replace('__HOME__', home)

# store values in cookie
cookie['pos'] = pos
cookie['grump'] = grump
cookie['cave1'] = cave1
cookie['cave2'] = cave2
cookie['bat1'] = bat1
cookie['bat2'] = bat2
cookie['maze0'] = maze[0]
cookie['maze1'] = maze[1]
cookie['maze2'] = maze[2]
cookie['maze3'] = maze[3]
cookie['maze4'] = maze[4]
cookie['maze5'] = maze[5]
cookie['maze6'] = maze[6]
cookie['maze7'] = maze[7]
cookie['maze8'] = maze[8]
cookie['maze9'] = maze[9]
cookie['maze10'] = maze[10]
cookie['maze11'] = maze[11]
cookie['maze12'] = maze[12]
cookie['maze13'] = maze[13]
cookie['maze14'] = maze[14]
cookie['maze15'] = maze[15]
cookie['maze16'] = maze[16]
cookie['maze17'] = maze[17]
cookie['maze18'] = maze[18]
cookie['maze19'] = maze[19]
cookie['first_run'] = first_run
print(cookie)

print('Content-Type: text/html')
print()

print('<html><body>')

# print positions
print("cave", cave1, cave2, "bat", bat1, bat2, "grump", grump)
print("pos", pos)
print('<p>')
for i in range(0, 19):
    print(maze[i])
    print('<br>')
print('<p>')

# print text
print("You are in room ", maze[pos][0])
print('<p>')
print("You can go to ", maze[pos][1])

# print forms
print(form_output)

print('</body></html>')
