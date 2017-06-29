#import timeit
CONST_MAX = 100000

def printPairs(arr, arr_size, sum):
	# initialize hash map
	binmap = [0]*CONST_MAX

	for i in range(0,arr_size):
		temp = sum-arr[i]
		if(temp>=0 and binmap[temp] == 1):
			print "Pair with given sum is", arr[i], "and", temp
		binmap[arr[i]]=1
"""
def wrapper(func, *args, **kwargs):
	def wrapped():
		return func(*args, **kwargs)
	return wrapped
"""
# driver program to check above function
A = [1,4,45,6,10,-8]
n = 16
print "The sum is ", n
printPairs(A, len(A), n)