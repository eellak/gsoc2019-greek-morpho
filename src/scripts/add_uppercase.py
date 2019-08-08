import sys
import re

if len(sys.argv) == 1:
	in_file = sys.stdin
	
elif len(sys.argv) == 2:
	in_file = open(sys.argv[1],"r")
else:
	sys.exit("ERROR: Usage %s [input_dictionary]" % sys.argv[0],file=sys.stderr)

line = in_file.readline()

se_atona = {
	'Ά' : 'Α',
	'Έ' : 'Ε',
	'Ή' : 'Η',
	'Ί' : 'Ι',
	'Ό' : 'Ο',
	'Ώ' : 'Ω',
	'Ύ' : 'Υ',
	'ΰ' : 'ϋ', # we add these 2 because python produces not accepted upper case
	'ΐ' : 'ϊ'
	
}

def no_accent(s):
	for i in range(len(s)):
		if s[i] in se_atona:
			s = s[:i] + se_atona[s[i]] + s[i+1:]
	return s

while line != '':
	# άι -> ΑΪ
	tmp = re.sub(r'(?<=[άΆύΎόΌέΈ])[ιΙ]', 'Ϊ',line,re.UNICODE)
	tmp = re.sub(r'(?<=[άΆόΌ])[υΥ]', 'Ϋ',tmp,re.UNICODE)
	tmp = no_accent(tmp)
	tmp = tmp.upper()
	tmp = no_accent(tmp)
	print(line,end='')
	if tmp != line:
		print(tmp,end='')
	line = in_file.readline()
