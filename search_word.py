import json
data = json.load(open("index.json"))

def find_word(w):
	w = w.lower()
	if w in data:
		return w
	else:
		print("word not found")

def is_word(w):
	w = w.lower()
	if w in data:
		return True
	else:
		return False
