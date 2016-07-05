
def isPalindrom(stringNum):
	if len(stringNum) == 1:
		return True
	elif len(stringNum) == 2:
		if stringNum[0] == stringNum[1]:
			return True
		else:
			return False
	else:
		if stringNum[0] == stringNum[-1]:
			return isPalindrom(stringNum[1:-1])
		else:
			return False

def main():
	loop()

def loop():
	biggest = 0
	for x in range(100, 999):
		for y in range(100,999):
			big = x * y
			stringNum = str(big)
			if isPalindrom(stringNum):
				if biggest < big:
					biggest = big
	print biggest

main()
