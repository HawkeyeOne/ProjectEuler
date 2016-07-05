

def isDivisible(num):
	check = True
	for x in range(1,21):
		if num % x == 0:
			check = True
		else:
			return False
	return check
			

def main():
	i = 1 
	found = True
	while(found):
		print "Trying %d" %(i)
		if isDivisible(i):
			print i
			found = False
		else:
			i = i + 1

main()
