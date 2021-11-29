#import enchant
#d = enchant.Dict("en_US")
import json
data = json.load(open("index.json"))

# Python program to print all permutations with
# duplicates allowed

def toString(List):
	return ''.join(List)

# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
def permute(a, l, r, result_table):

	if l == r:
		n = len(a)
		if (n <= 3):
			return
		str = toString(a)
		if(d.check(str) == True):
			#print(str)
			if(str in result_table):
				return
			result_table.append(str)
			#print(str);
		permute(a[0:n-1], 0, n-2, result_table)
	else:
		for i in range(l, r + 1):
			a[l], a[i] = a[i], a[l]
			permute(a, l + 1, r, result_table)
			a[l], a[i] = a[i], a[l] # backtrack


def get_n_anagrams(str_arr, c_special, min_length, result_table):
	
	for dstr in data:
		dword = list(dstr)
		has_c_special = False
		contains_only_str = True
		for chr in dword:
			if chr not in str_arr:
				contains_only_str = False
				break
			if (chr == c_special):
				has_c_special = True
		
		if(c_special != 0 and has_c_special and contains_only_str):
			if (len(dstr) >= min_length):
					result_table.append(dstr)
		elif c_special == 0 and contains_only_str:
			if (len(dstr) >= min_length):
				result_table.append(dstr)
				
def cheat_scrabble(str_arr,result_table):
	for dstr in data:
		dword = list(dstr)
		n = len(str_arr)
		used = [0] * n
		contains_only_str = True
		for d_chr in dword:
			in_list = False
			for i in range(0,n):
				c = str_arr[i]
				if(d_chr == c and used[i] == 0):
					#used[i] = 0
					used[i] = 1
					in_list = True
					break
			
			if in_list == False:
				contains_only_str = in_list
				break
				
		if(contains_only_str):
			result_table.append(dstr)
				
			
			
			
		