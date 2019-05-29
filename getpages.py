import sys
from mediawiki import MediaWiki
from parse import AdjParser,parse_noun,wword,conn,is_complete
from verb import parse_verb
mw = MediaWiki(url='https://el.wiktionary.org/w/api.php',timeout=100.0)

NotDetectedAdj = open("NotDetectedAdj.dic","a")

print('Getting lemmas')

if len(sys.argv) == 2 and sys.argv[1] == 'production':
	nouns = mw.categorymembers(category='Ουσιαστικά (ελληνικά)',results=100000,subcategories=False)
	proper_nouns = mw.categorymembers(category='Κύρια ονόματα (ελληνικά)',results=100000,subcategories=False)
	adj = mw.categorymembers(category='Επίθετα (ελληνικά)',results=100000,subcategories=False)
	verbs = mw.categorymembers(category='Ρήματα (ελληνικά)',results=1000000,subcategories=False)
	num_download = 1000000
else:
	#Tests
	adj = ['ανώμαλος','πράσινος','ταχύς','αβάζος','διπύρηνος','μακρύς']
	nouns = ['τελωνείο','σύμμαχος','ανώμαλος','διάκεντρος','Ααρών','σκληρός δίσκος','Αρμαγεδδώνας','ρουλεμάν','Κολοκοτρώνης','γιατρός','σεληνοτοπογράφος','Ανδρέας','Μαρία','Αθήνα','Λάρισα','Ελλάδα','δέκα','άνθρακας','εδεσματολόγιο']
	verbs = ['λύνω','αγαπώ','διασπώ']
	proper_nouns = []
	num_download = 1

prs = mw.categorymembers(category='Προθέσεις (ελληνικά)',results=num_download,subcategories=False)
advs = mw.categorymembers(category='Επιρρήματα (ελληνικά)',results=num_download,subcategories=False)
#particles = mw.categorymembers(category='Μετοχές (ελληνικά)',results=10,subcategories=False)#είτε άκλιτες,είτε κλιτές πχ χαρούμενος
acr = mw.categorymembers(category='Συντομομορφές (ελληνικά)',results=num_download,subcategories=False)#Άλλο ακρονύμιο,άλλο αρκτικόλεξο

padj = AdjParser()

print(len(nouns),' nouns')
print(len(proper_nouns),' proper nouns')
print(len(adj),' adjectives')
print(len(verbs),' verbs')
print(len(prs),' prepositions')
print(len(advs),' adverbs')
print(len(acr),' acronyms')
nouns = nouns + proper_nouns

for title in verbs:
	if is_complete(title,['VERB']):
		continue
	page = mw.page(title)
	print('parsing ' + title,end='')
	html = page.html
	parse_verb(html,title)
	conn.commit()
	print()

#Ταχυς produces wrong?
for title in adj:
	if is_complete(title,['ADJ']):
		continue
	page = mw.page(title)
	print('parsing ' + title,end='')
	html = page.html
	padj.lemma = title
	padj.feed(html)
	if padj.detected == False:
		print('[[' + title + ']]',file=NotDetectedAdj)
		wword(title,title,'ADJ',tags='Incomplete')
	conn.commit()
	print()

def id_add(string,tag):
	if tag not in string:
		if string != '':
			string += ' '
		string += tag
	return string

for title in nouns:
	if is_complete(title,['NOUN','PROPN']):
		continue
	if is_complete(title,'PROPN'):#also top ant??
		continue
	page = mw.page(title)
	print('parsing ' + page.title,end='')
	html = page.html
	categories = page.categories
	part = 'NOUN'
	tag = ''
	for c in categories:
		if c == 'Κατηγορία:Κύρια ονόματα (ελληνικά)':
			part = 'PROPN'
	for c in categories:
		if c == 'Κατηγορία:Πολυλεκτικοί όροι (ελληνικά)':
			tag = id_add(tag,'PolyTerm')
		if c == 'Κατηγορία:Πόλεις της Ελλάδας (ελληνικά)':
			tag = id_add(tag,'Top')
			tag = id_add(tag,'City')
			tag = id_add(tag,'Greece')
		if c == 'Κατηγορία:Ευρωπαϊκές πρωτεύουσες (ελληνικά)':
			tag = id_add(tag,'Top')
			tag = id_add(tag,'Capital')
			tag = id_add(tag,'Europe')
		if c in ['Κατηγορία:Γυναικεία ονόματα (ελληνικά)','Κατηγορία:Ανδρικά ονόματα (ελληνικά)']:
			tag = id_add(tag,'Ant')
		if c == 'Κατηγορία:Χώρες (ελληνικά)':
			tag = id_add(tag,'Top')
			tag = id_add(tag,'Country')
		if c == 'Κατηγορία:Ευρωπαϊκή Ένωση (ελληνικά)':
			tag = id_add(tag,'Top')
			tag = id_add(tag,'Top')
			tag = id_add(tag,'EuropeanUnion')
		if c == 'Κατηγορία:Χημικά στοιχεία στα ελληνικά':
			tag = id_add(tag,'Element')
		if c == 'Κατηγορία:Πληροφορική_(ελληνικά)':
			tag = id_add(tag,'Informatics')
			
	parse_noun(html,title,part,tag)
	conn.commit()
	print()

for word in prs:
	if is_complete(word,['PRON']):
		continue
	wword(word,word,'PRON')
	
for word in advs:
	if is_complete(word,['ADV']):
		continue
	wword(word,word,'ADV')
#ACR = NOUN + Abbr=Yes??
#Also add tag αρκτικ ακρονυμιο
for word in acr:
	if is_complete(word,['acr']):
		continue
	wword(word,word,'acr')
#TODO MORIA PART Αριθμητικά
conn.commit()
