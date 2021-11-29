from permute_def import get_n_anagrams
from permute_def import cheat_scrabble

string = "nvaomit"

result_table = []
get_n_anagrams(list(string),'t',4,result_table)
#print(result_table)
print("there are",len(result_table), "results")
sorted_nanagram = []
for word in result_table:
	sorted_nanagram.append([word, len(word)])
sorted_nanagram.sort(key = lambda x:x[1])
print(sorted_nanagram[-2])

scrabble_result = []
cheat_scrabble(list(string),scrabble_result)
#print(scrabble_result)

result_len = []
for i in range(0,len(scrabble_result)):
	result_len.append([scrabble_result[i],len(scrabble_result[i])])
result_len.sort(key = lambda x: x[1])
#print(result_len)
