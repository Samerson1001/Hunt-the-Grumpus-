#!/usr/bin/env python3

import cgi
form = cgi.FieldStorage()

home_form = """
    <form method="get" action="/cgi-bin/GrumpusWebStable.py">
        What you wanna do (move/shoot): <input type="text" name="home">
        <input type="submit" value="Submit">
    </form>
"""

move_form = """
   <form method="get" action="/cgi-bin/GrumpusWebStable.py">
        Go to: <input type="text" name="move">
        <input type="hidden" name="home" value="__HOME__">
        <input type="submit" value="Submit">
    </form> 
"""

shoot_form = """
   <form method="get" action="/cgi-bin/GrumpusWebStable.py">
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

print('Content-Type: text/html')
print() 

print('<html><body>')
print(output)
print('</body></html>')
