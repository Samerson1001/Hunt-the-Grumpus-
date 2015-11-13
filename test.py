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

print("You are in room ", maze[0][0])
print("You can go to ", maze[0][1])