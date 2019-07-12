import sys
import re

words = {}

min_count_found = 1

in_file = sys.stdin
line = in_file.readline()

# συν διαλυτικά
se_tonismena = {
	'α' : 'ά',
	'ε' : 'έ',
	'η' : 'ή',
	'ι' : 'ί',
	'ο' : 'ό',
	'ω' : 'ώ',
	'υ' : 'ύ',
	'ϋ' : 'ΰ',
	'ϊ' : 'ΐ'
}

# first pass, put words into dictionary

while line != '':
	line = line.strip()
	if line.strip() in words:
		words[line] += 1
	elif line != '':
		words[line] = 1
	line = in_file.readline()

# second pass, remove probably wrong words
word_list = []

for x,y in words.items():
	
	should_be_put = True
	
	if y < min_count_found:
		continue
	
	elif re.fullmatch("[αβγδεζηθικλμνξοπρστυφχψωςϋϊ]*[αεηιυοωϋϊ]+[βγδζθκλμνξπρστφχψς]+[αεηιυοωϋϊ]+[αβγδεζηθικλμνξοπρστυφχψωςϋϊ]*",x) is not None:
		# print('#άτονο#',x)
		continue
	# if there is the same word in lower case, skip it	
	elif x != x.lower():
		if x.lower() in words: 
			continue
		lowered = x.lower()

		if lowered[-1] == 'σ':
			lowered = lowered[:len(lowered)-1] + 'ς'

		for i in range(len(lowered)):
			if lowered[i] in se_tonismena:
				tmp = lowered[:i] + se_tonismena[lowered[i]] + lowered[i+1:]
				# print(x,tmp)
				if tmp in words:
					should_be_put = False
				
				# first character can be upper
				tmp = lowered[0].upper() + lowered[1:i] + se_tonismena[lowered[i]] + lowered[i+1:]
				if tmp in words:
					should_be_put = False

	if should_be_put:
		word_list.append((x,y))

for x,y in sorted(word_list):
	print(x,y)
