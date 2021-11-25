import enchant
from permute_def import permute

string = "AABBCC"


n = len(string)
a = list(string)
permute(a,0,n-1)