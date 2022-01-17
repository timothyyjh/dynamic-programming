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