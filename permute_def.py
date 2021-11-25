import enchant
d = enchant.Dict("en_US")
# Python program to print all permutations with
# duplicates allowed

def toString(List):
	return ''.join(List)

# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
def permute(a, l, r):

	if l == r:
		n = len(a)
		if (n <= 1):
			return
		str = toString(a)
		
		if(d.check(str) == True):
			print(str)
		permute(a[0:n-1],0,n-2)
	else:
		for i in range(l, r + 1):
			a[l], a[i] = a[i], a[l]
			permute(a, l + 1, r)
			a[l], a[i] = a[i], a[l] # backtrack
