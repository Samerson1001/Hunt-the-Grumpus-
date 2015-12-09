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

cave1, cave2, bat1, bat2, pos, grump = random.sample(num, 6)

caves = [
		  cave1, cave2
		]
bats = [
		  bat1, bat2
	   ]	

alive = True
dead = False
while alive:
	check = True
	while check:
		checkon = False
		if maze[pos][0] == grump:
			print("The grump got ya")
			dead = True
			alive = False
			
		test1 = True
		if maze[pos][0] == bats[0] or maze[pos][0] == bats[1]:
			print("**************************")
			print("Ew gross. Bats")
			while maze[pos][0] == bats[0]:
				test1 = False
				checkon = True
				pos = random.randint(0,19)
			if test1:
				while maze[pos][0] == bats[1]:
					checkon = True
					pos = random.randint(0,19)
		check = False
		if checkon == True:
				check = True

	if maze[pos][0] == caves[0] or maze[pos][0] == caves[1]:
		print("Thou Art Dead (cave)")
		dead = True
		alive = False

	if not dead:
		print("cave", cave1, cave2, "bat", bat1, bat2, "grump", grump)
		print("**************************")
		i = 0
		k = 0
		while i < 3:
			k = 0
			while k < 2:
				if maze[pos][1][i] == caves[k]:
					print("You feel the breeze of a cave\n")
				if maze[pos][1][i] == bats[k]:
					print("You hear the flapping of wings\n")
				k += 1
			if maze[pos][1][i] == grump:
					print("You smell the stench of the grump\n")
			i += 1
			
		print("You are in room ", maze[pos][0])
		print("You can go to ", maze[pos][1])
		choice = input("What you wanna do (move/shoot): ")
		if choice == "move":
			newpos = input("Go to: ")
			newpos = int(newpos)
			
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
			else:
				print("**************************")
				print("Invalid room")
		elif choice == "shoot":
			NumRooms = input("How many rooms?: ")
			NumRooms = int(NumRooms)
			shots = []
			arrowPos = pos
			for var in range(NumRooms):
				room = input("Room: ")
				room = int(room)
				shots.append(room)
			for roomVar in range(len(shots)):
				thisthing = shots[roomVar]
				if thisthing in maze[arrowPos][1]:
					bahl = 0
					while maze[bahl][0] != shots[roomVar]:
						bahl += 1
					arrowPos = bahl
					if maze[arrowPos][0] == grump:
						print("It is done")
						alive = False
						dead = True
			print("Twang")
		elif choice == "1337":#"totallyawesomehackerthing1337":
			print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
			user = input("User_ ")
			if user == "1001":#"c00lguy1":
				password = input("Password_ ")
				if password == "0110":#"n0b":
					print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
					print("Dev menu")
					print("--------")
					guh = 0
					while guh < 20:
						print(maze[guh])
						guh+=1
					print("cave ", cave1, cave2, "\nbat  ", bat1, bat2, "\ngrump", grump, "pos", pos )
					
					pause = input("")

		else:
			print("**************************")
			print("Invalid action")


	


