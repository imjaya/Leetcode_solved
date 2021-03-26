# Python program to print
# print all primes in a range
# using concept of Segmented Sieve
from math import floor, sqrt

# This functions finds
# all primes smaller than limit
# using simple sieve of eratosthenes.
# It stores found
# primes in list prime[]


def simpleSieve(limit, primes):
	mark = [False]*(limit+1)

	for i in range(2, limit+1):
		if not mark[i]:

			# If not marked yet,
			# then its a prime
			primes.append(i)
			for j in range(i, limit+1, i):
				mark[j] = True


# Finds all prime numbers
# in given range using
# segmented sieve
def primesInRange(low, high):
	limit = floor(sqrt(high)) + 1
	primes = list()
	simpleSieve(limit, primes)
	n = high - low + 1
	mark = [False]*(n+1)
	for i in range(len(primes)):
		loLim = floor(low/primes[i]) * primes[i]
		if loLim < low:
			loLim += primes[i]
		if loLim == primes[i]:
			loLim += primes[i]

		for j in range(loLim, high+1, primes[i]):
			mark[j-low] = True
	result=[]
	for i in range(low, high+1):
		if not mark[i-low]:
			result.append(i)
	return result


# Driver code
low = 5
high =5
primesInRange(low, high)
