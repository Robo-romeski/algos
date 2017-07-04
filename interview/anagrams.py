# Anagram method
"""
def anagram(word):
	if len(word) < 2:
		yield word
	else:
		for i, letter in enumerate(word):
			if not letter in word[:1]:
				for j in anagram(word[:1]+word[i+1:]):
					yield j+letter

if __name__ == '__main__':
	for i in anagram("71717"):
		print i
"""
import itertools


perms = itertools.permutations([7,17,17,3,43,131,432])

print list(perms)