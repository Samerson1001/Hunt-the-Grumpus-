#!/usr/bin/env python3

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
	    [num[12],[num[11],num[10],num[19]]],
	    [num[13],[num[4],num[14],num[12]]],
	    [num[14],[num[13],num[5],num[15]]],
	    [num[15],[num[14],num[16],num[19]]],
	    [num[16],[num[6],num[15],num[17]]],
	    [num[17],[num[16],num[18],num[8]]],
	    [num[18],[num[10],num[17],num[19]]],
	    [num[19],[num[18],num[15],num[12]]],
	   ]
cave1 = random.randint(1,19)
cave2 = random.randint(1,19)
bat1 = random.randint(1,19)
bat2 = random.randint(1,19)
grump = random.randint(1,19)
while cave1 == cave2 or cave1 == bat1 or cave1 == bat2 or cave2 == bat1 or cave2 == bat2 or	bat1 == bat2:
	cave2 = random.randint(1,19)
	bat1 = random.randint(1,19)
	bat2 = random.randint(1,19)
caves = [
		  cave1, cave2
		]
bats = [
		  bat1, bat2
	   ]
pos = 0 #  pos needs to be equal to where the maze value / room is equal to 0. not maze[0]
alive = 1




# -------------------------------- web ----------------------------------------
#!/usr/bin/env python3

print('Content-Type: text/html')
print()

print('<html><body>')
print('hello world')
print('</body></html>')

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

if 'home' not in form or home == '':
    output = home_form
    move = ''
    shoot = ''
elif home == 'move':
    if 'move' not in form or move == '':
        home = ''
        output = move_form.replace('__HOME__', home)
    else:
        move = float(form.getvalue('move'))
elif home == 'shoot':
    if 'shoot' not in form or shoot == '':
        home = ''
        output = shoot_form.replace('__HOME__', home)
    else:
        shoot = float(form.getvalue('shoot'))
else:
    output = home_form.replace('__HOME__', home)

print('<html><body>')
print(output)
print('</body></html>')
