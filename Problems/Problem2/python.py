def checkEven(num):
	return (num % 2) == 0

prev = 0
curr = 0
total = 0
i = 1
while(i < 4000000):
	if(i==1):
		curr = i
		prev = i
		i = curr + prev
	else:
		i = curr + prev
		prev = curr
		curr = i
		if checkEven(i):
			total += i	

print total
