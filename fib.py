# This fibonacci function utilizes the technique of memoization so that 
# subsequent trees in the calculation that includes the same equation
# will make use of the sum that is already stored in the dictionary.
# This ensures that the time complexity aspect is efficient.

def fib(n, memo={}):
	if n in memo:
		return memo[n]
	if n == 0:
		return 0
	if n <= 2:
		return 1
	memo[n] = fib(n-1, memo) + fib(n-2, memo)
	return memo[n]

# x = 0
# while x < 100:
# 	print(fib(x))
# 	x += 1