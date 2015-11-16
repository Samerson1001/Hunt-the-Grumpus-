import random

num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
	   11, 12, 13, 14, 15, 16, 17, 18, 19]
random.shuffle(num)
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

pos = 0

while 1:
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
		print("Invalid room")












