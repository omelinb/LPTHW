def list(x, y):	
	i = 0
	numbers = []

	while i < x:
		print "At the top i is %d" % i
		numbers.append(i)

		i = i + y
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i


	print "The numbers: "

	for num in numbers:
		print num

list(int(raw_input("> ")), int(raw_input("> ")))