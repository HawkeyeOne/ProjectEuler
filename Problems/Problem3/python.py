

def isPrime(num):
	i = 5
	if num == 2 or num == 3:
		return True
	elif num % 2 == 0 or num % 3 == 0:
		return False	
	while i*i <= num:
		if num % i == 0 or num % (i+2) == 0:
			return False
		i = i + 6
	return True

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def main():
	num = 600851475143
	listOfFactors = list(factors(num)) 
	highestPrime = 0
	for x in listOfFactors:
		print x
		if x > highestPrime:
			if isPrime(x):
				highestPrime = x
	print highestPrime
	print isPrime(highestPrime)

main()
	
	
