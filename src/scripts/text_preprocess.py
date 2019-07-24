import re
import sys

in_file = sys.stdin

line = in_file.readline()

alphabet = '[ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩαβγδεζηθικλμνξοπρστυφχψωςάέήίόύώΐΰϋϊἱΆΈΉΊΌΎΏΫΪ]'

mapping = { 'o' : 'ο', 'O' : 'Ο', 'a' : 'α', 'A' : 'Α', 'B' : 'Β',
            'v' : 'ν', 'E' : 'Ε', 'M' : 'Μ', 'N' : 'Ν', 'K' : 'Κ',
            'x' : 'χ', 'X' : 'Χ', 'Z' : 'Ζ', 'T' : 'Τ', 'Y' : 'Υ',
            'P' : 'Ρ', 'I' : 'Ι', 'H' : 'Η'}
count = 0

def replace_function(m):
	global count

	if m.group(2) in mapping:
		#print(m.group(1), m.group(2),m.group(3))
		count += 1
		return m.group(1) + mapping[m.group(2)] + m.group(3)
	else:
		print(m.group(0),file=sys.stderr)
		return m.group(0)

while line:
	# english o to greek ο
	line = re.sub(r'(%s*)([a-zA-Z])(%s+)' % (alphabet,alphabet), replace_function,line,re.UNICODE) 

	print(line,end='')

	line = in_file.readline()

print('%s Total substitutions' % count,file=sys.stderr)
