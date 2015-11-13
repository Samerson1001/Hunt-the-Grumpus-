import random

numbers[0, 1, 2, 3, 4]
letters[a, b, c, d, e]
for letter in letters:
	i = random.randint(0, len(numbers)- 1)
	letters[letter] = numbers[i]
	numbers.pop(i)






maze = [
		[a,[e,f,g]],
	    [1,[4,5,6]]
	   ]


print(maze[1][1])