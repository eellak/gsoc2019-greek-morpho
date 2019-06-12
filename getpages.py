# pip3 install pymediawiki
# http://pymediawiki.readthedocs.io/en/latest/code.html

import sys
import re
from mediawiki import MediaWiki
from parse import AdjParser,parse_noun,wword,conn,is_complete,form_exists,parse_code,cur
from verb import parse_verb
mw = MediaWiki(url='https://el.wiktionary.org/w/api.php',timeout=100.0)

NotDetectedAdj = open("NotDetectedAdj.dic","a")

print('Getting lemmas')

if len(sys.argv) == 2 and sys.argv[1] == 'production':
	nouns = mw.categorymembers(category='Ουσιαστικά (νέα ελληνικά)',results=100000,subcategories=False)#πρέπει να βάλουμε πολυλεκτικούς όρους
	proper_nouns = mw.categorymembers(category='Κύρια ονόματα (νέα ελληνικά)',results=100000,subcategories=False)
	adj = mw.categorymembers(category='Επίθετα (νέα ελληνικά)',results=100000,subcategories=False)
	verbs = mw.categorymembers(category='Ρήματα (νέα ελληνικά)',results=1000000,subcategories=False)
	participles = mw.categorymembers(category='Μετοχές (νέα ελληνικά)',results=100000,subcategories=False)#είτε άκλιτες,είτε κλιτές πχ χαρούμενος
	num_download = 1000000
else:
	#Tests
	adj = ['ομορφότερος','μέγιστος','ανώμαλος','πράσινος','ταχύς','αβάζος','διπύρηνος','μακρύς']
	nouns = ['τελωνείο','σύμμαχος','ανώμαλος','διάκεντρος','Ααρών','σκληρός δίσκος','Αρμαγεδδώνας','ρουλεμάν','Κολοκοτρώνης','γιατρός','σεληνοτοπογράφος','Ανδρέας','Μαρία','Αθήνα','Λάρισα','Ελλάδα','δέκα','άνθρακας','εδεσματολόγιο']
	verbs = ['αγριοκοιτάω','αγριοκοιτιέμαι','παραποιώ','φρενάρω','λύνω','αγαπιέμαι','αγαπώ','είμαι','διασπώ']
	participles = ['αγαπημένος','αγαπώντας','φρενάροντας','ζητούμενος']
	proper_nouns = []
	num_download = 20

prs = mw.categorymembers(category='Προθέσεις (νέα ελληνικά)',results=num_download,subcategories=False)
advs = mw.categorymembers(category='Επιρρήματα (νέα ελληνικά)',results=num_download,subcategories=False)
acr = mw.categorymembers(category='Συντομομορφές (νέα ελληνικά)',results=num_download,subcategories=False)#Άλλο ακρονύμιο,άλλο αρκτικόλεξο
protheseis = mw.categorymembers(category='Προθέσεις (νέα ελληνικά)',results=num_download,subcategories=False)
moria = mw.categorymembers(category='Μόρια (νέα ελληνικά)',results=num_download,subcategories=False)
num = mw.categorymembers(category='Αριθμητικά (νέα ελληνικά)',results=num_download,subcategories=False) # τακτικά, απόλυτα
epifonimata = mw.categorymembers(category='Επιφωνήματα (νέα ελληνικά)',results=num_download,subcategories=False)

print(len(nouns),' nouns')
print(len(proper_nouns),' proper nouns')
print(len(adj),' adjectives')
print(len(verbs),' verbs')
print(len(prs),' prepositions')
print(len(advs),' adverbs')
print(len(acr),' acronyms')
print(len(num),' num')

nouns = nouns + proper_nouns

def get_page(title):
	p = mw.page(title)
	code = p.content
	parse_code(title,code)
	return p


for title in verbs:
	if is_complete(title,['VERB']):
		continue
	#μπορεί να είναι παθητικό και να έχουμε βάλει ήδη το ενεργητικό λήμμα
	if form_exists(title,'VERB'):
		continue
	page = get_page(title)
	print('parsing ' + title,end='')
	html = page.html
	code = page.content
	parse_verb(html,code,title)
	conn.commit()
	print()

for title in participles:
	if is_complete(title,['VERB']):
		continue
	print('title %s:' % title)
	padj = AdjParser()
	padj.part = "VERB"
	page = get_page(title)
	print('parsing ' + title,end='')
	html = page.html
	lemma = title
	if form_exists(title,'VERB'):#Αν το έχουμε βάλει
		cur.execute("DELETE FROM words WHERE lemma = ?;" , (title,))
		cur.execute('SELECT lemma FROM words WHERE form = ? AND pos = \'VERB\'',(title,))
		r = cur.fetchall()
		lemma = r[0][0]
        #ΤΟΔΟ βάλε ως λήμμα το ρήμα
	res = re.search('μετοχή παθητικού (ενεστώτα|παρακειμένου) του ρήματος \<a href=\"[^\"]+?\" title=\"(?P<LEMMA>[^\"]+?)\"\>.+?\<\/a>',html,re.UNICODE|re.DOTALL)

	if  res != None:
		lemma = res.group('LEMMA')
	res = re.search('μετοχή\<\/a\> \<a href=\"\/wiki\/\%CE\%B5\%CE\%BD\%CE\%B5\%CF\%83\%CF\%84\%CF\%8E\%CF\%84\%CE\%B1\%CF\%82\" title=\"ενεστώτας\"\>ενεστώτα\<\/a\> του \<i\>\<a href=\"[^\"]+?\" title=\"(?P<LEMMA>[^\"]+?)\">[^\"]+?\<\/a\>',html,re.UNICODE|re.DOTALL)
	if res != None:
		lemma = res.group('LEMMA')
	padj.lemma = lemma
	padj.greek_pos = 'METOXI_PP'
	padj.feed(html)
	#if padj.detected == False:
	#	print('[[' + title + ']]',file=NotDetectedAdj)
	#	wword(title,title,'VERB',tags='Incomplete') # TODO
	conn.commit()
	print()

for title in adj:
	if is_complete(title,['ADJ']):
		continue
	padj = AdjParser()
	page = get_page(title)
	print('parsing %s' % title,end='')
	html = page.html
	sygritikos = "title=\"συγκριτικός\"\>συγκριτικός\</a\> βαθμός του \<i\>\<a href=\"/wiki/.*?\" title=\".*?\"\>(?P<lemma>[ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩαβγδεζηθικλμνξοπρστυφχψωςάέήίόύώΐΰϋϊἱΆΈΉΊΌΎΏΫΪ]+)\</a\>"
	syg = re.search(sygritikos,html,re.UNICODE)
	if syg != None:
		print(' συγκριτικός: ' + syg.group("lemma"),end='')
		title = syg.group("lemma")
		padj.degree = "Cmp"

	uperthetikos = "title=\"υπερθετικός\"\>υπερθετικός\</a\> βαθμός του\<i\> \<a href=\"/wiki/.*?\" title=\".*?\"\>(?P<lemma>[ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩαβγδεζηθικλμνξοπρστυφχψωςάέήίόύώΐΰϋϊἱΆΈΉΊΌΎΏΫΪ]+)\</a\>"
	sup = re.search(uperthetikos,html,re.UNICODE)
	if sup != None:
		print(' υπερθετικός: ' + sup.group("lemma"),end='')
		title = sup.group("lemma")
		padj.degree = "Sup"

	padj.lemma = title
	padj.part = 'ADJ'
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
	page = get_page(title)
	print('parsing ' + page.title,end='')
	html = page.html
	categories = page.categories
	part = 'NOUN'
	tag = ''
	#Αν ο τίτλος έχει παραπάνω από μία λέξεις βάλε PolyTerm
	for c in categories:
		if c == 'Κατηγορία:Κύρια ονόματα (νέα ελληνικά)':
			part = 'PROPN'
	for c in categories:
		if c == 'Κατηγορία:Πολυλεκτικοί όροι (νεα ελληνικά)':
			tag = id_add(tag,'PolyTerm')
		if c == 'Κατηγορία:Πόλεις της Ελλάδας (ελληνικά)':
			tag = id_add(tag,'Top')
			tag = id_add(tag,'City')
			tag = id_add(tag,'Greece')
		if c == 'Κατηγορία:Ευρωπαϊκές πρωτεύουσες (ελληνικά)':
			tag = id_add(tag,'Top')
			tag = id_add(tag,'Capital')
			tag = id_add(tag,'Europe')
		if c in ['Κατηγορία:Γυναικεία ονόματα (νέα ελληνικά)','Κατηγορία:Ανδρικά ονόματα (νέα ελληνικά)']:
			tag = id_add(tag,'Ant')
		if c == 'Κατηγορία:Χώρες (ελληνικά)':
			tag = id_add(tag,'Top')
			tag = id_add(tag,'Country')
		if c == 'Κατηγορία:Ευρωπαϊκή Ένωση (ελληνικά)':
			tag = id_add(tag,'Top')
			tag = id_add(tag,'Top')
			tag = id_add(tag,'EuropeanUnion')
		if c == 'Κατηγορία:Χημικά στοιχεία (ελληνικά)':
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

for word in protheseis:
	if is_complete(word,['ADP']):
		continue
	wword(word,word,'ADP')

for word in moria:
	if is_complete(word,['PART']):
		continue
	wword(word,word,'PART')

for word in epifonimata:
	if is_complete(word,['INTJ']):
		continue
	wword(word,word,'INTJ')

# we assume noun as in UD_GREEK
for word in acr:
	if is_complete(word,['NOUN']):
		continue
	wword(word,word,'NOUN',tags='Abbr')

# Αριθμητικά
# TODO τακτικά κτλ
for title in num:
	if is_complete(title,['NUM']):
		continue
	padj = AdjParser()
	print('parsing %s'% title)
	page = get_page(title)
	html = page.html
	padj.lemma = title
	padj.part = 'NUM'
	padj.feed(html)
	if padj.detected == False:
		wword(title,title,'NUM')
	conn.commit()

conn.commit()
