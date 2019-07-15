# pip3 install pymediawiki
# http://pymediawiki.readthedocs.io/en/latest/code.html

# TODO διαγράφω
import sys
import re
from mediawiki import MediaWiki
from parse import AdjParser, parse_noun, wword, conn, is_complete, form_exists, parse_code, cur
from verb import parse_verb
mw = MediaWiki(url='https://el.wiktionary.org/w/api.php',timeout=100.0)

NotDetectedAdj = open("NotDetectedAdj.dic","a")

print('Getting lemmas')

if len(sys.argv) == 2 and sys.argv[1] == 'production':
	nouns = mw.categorymembers(category='Ουσιαστικά (νέα ελληνικά)', results=100000, subcategories=False)#πρέπει να βάλουμε πολυλεκτικούς όρους
	proper_nouns = mw.categorymembers(category='Κύρια ονόματα (νέα ελληνικά)', results=100000,subcategories=False)
	adj = mw.categorymembers(category='Επίθετα (νέα ελληνικά)', results=100000, subcategories=False)
	verbs = mw.categorymembers(category='Ρήματα (νέα ελληνικά)', results=1000000, subcategories=False)
	participles = mw.categorymembers(category='Μετοχές (νέα ελληνικά)', results=100000, subcategories=False)#είτε άκλιτες,είτε κλιτές πχ χαρούμενος
	num_download = 1000000
else:
	# Tests
	adj = ['ομορφότερος','μέγιστος','ανώμαλος','πράσινος','ταχύς','αβάζος','διπύρηνος','μακρύς']
	nouns = ['εισπνοή','βόλος','Βιβή','τελωνείο','δάκρυ','σύμμαχος','ανώμαλος','διάκεντρος','Ααρών','σκληρός δίσκος','Αρμαγεδδώνας','ρουλεμάν','Κολοκοτρώνης','γιατρός','σεληνοτοπογράφος','Ανδρέας','Μαρία','Αθήνα','Λάρισα','Ελλάδα','δέκα','άνθρακας','εδεσματολόγιο']
	verbs = ['ζητώ','ανατινάζομαι','αλληλοεξουδετερώνομαι','διαγράφω','ενιδρύω','αγιάζω','αγριοκοιτάω','αγριοκοιτιέμαι','παραποιώ','φρενάρω','λύνω','αγαπιέμαι','αγαπώ','είμαι','διασπώ']
	participles = ['αναδυόμενος','διευκολύνοντας','δεινοπαθώντας','αγαπημένος','αγαπώντας','ζητούμενος']
	proper_nouns = []
	num_download = 20

prs = mw.categorymembers(category='Προθέσεις (νέα ελληνικά)', results=num_download, subcategories=False)
advs = mw.categorymembers(category='Επιρρήματα (νέα ελληνικά)', results=num_download, subcategories=False)
acr = mw.categorymembers(category='Συντομομορφές (νέα ελληνικά)', results=num_download, subcategories=False)#Άλλο ακρονύμιο,άλλο αρκτικόλεξο
protheseis = mw.categorymembers(category='Προθέσεις (νέα ελληνικά)', results=num_download, subcategories=False)
moria = mw.categorymembers(category='Μόρια (νέα ελληνικά)', results=num_download, subcategories=False)
num = mw.categorymembers(category='Αριθμητικά (νέα ελληνικά)', results=num_download, subcategories=False) # τακτικά, απόλυτα
epifonimata = mw.categorymembers(category='Επιφωνήματα (νέα ελληνικά)', results=num_download, subcategories=False)
rimatikoi_typoi = mw.categorymembers(category='Ρηματικοί τύποι (νέα ελληνικά)', results=num_download, subcategories=False)

print(len(nouns), ' nouns')
print(len(proper_nouns), ' proper nouns')
print(len(adj), ' adjectives')
print(len(verbs), ' verbs')
print(len(prs), ' prepositions')
print(len(advs), ' adverbs')
print(len(acr), ' acronyms')
print(len(num), ' num')

nouns = nouns + proper_nouns

# many passive verbs are in ρηματικοί τύποι
verbs_from_rimatikous_typous = [a for a in rimatikoi_typoi if a.endswith("ομαι") or a.endswith('ούμαι') or a.endswith("ιέμαι")]
print(len(verbs_from_rimatikous_typous), ' passive verbs in Ρηματικοί τύποι')

verbs += verbs_from_rimatikous_typous

def get_page(title):
	p = mw.page(title, auto_suggest=False)
	code = p.content
	parse_code(title, code)
	return p


for title in verbs:
	# μπορεί να είναι παθητικό και να έχουμε βάλει ήδη το ενεργητικό λήμμα
	if form_exists(title, 'VERB'):
		continue

	print('parsing %s:' % title, end='')
	page = get_page(title)

	html = page.html
	code = page.content
	parse_verb(html, code, title)
	conn.commit()
	print()

for title in participles:
	if is_complete(title, 'VERB'):
		continue

	# για τις περίεργες μετοχές -εις -ων
	cur.execute("SELECT lemma FROM words WHERE form = ? AND greek_pos = 'METOXI'", (title,))
	r = cur.fetchall()
	if len(r) != 0:
		continue
	
	print('parsing %s:' % title, end='')
	padj = AdjParser()
	padj.part = 'VERB'
	page = get_page(title)
	html = page.html
	lemma = title
	if form_exists(title, 'VERB'):# υπάρχει αλλά είναι Incomplete
		cur.execute("SELECT lemma FROM words WHERE form = ? AND pos = 'VERB'", (title,))
		r = cur.fetchall()
		if len(r) != 0:
			lemma = r[0][0]
			cur.execute("DELETE FROM words WHERE form = ?;", (title,))
			conn.commit()

	res = re.search(r'(καθώς|μετοχή (ενεργητικού|παθητικού) (ενεστώτα|παρακειμένου) του ρήματος)( |&#160;)<a href=\"[^\"]+?\" title=\"(?P<LEMMA>[^\"]+?)\">.+?</a>', html, re.UNICODE|re.DOTALL)

	if res is not None:
		lemma = res.group('LEMMA')

		cur.execute("SELECT lemma FROM words WHERE form = ? AND pos = 'VERB'", (lemma,))
		r = cur.fetchall()
		if len(r) != 0:
			lemma = r[0][0]
	res = re.search(r'μετοχή</a> <a href=\"/wiki/\%CE\%B5\%CE\%BD\%CE\%B5\%CF\%83\%CF\%84\%CF\%8E\%CF\%84\%CE\%B1\%CF\%82\" title=\"ενεστώτας\">ενεστώτα</a> του <i><a href=\"[^\"]+?\" title=\"(?P<LEMMA>[^\"]+?)\">[^\"]+?</a>', html, re.UNICODE|re.DOTALL)
	if res is not None:
		lemma = res.group('LEMMA')

	print(' lemma = %s ' % lemma, end='')
	padj.lemma = lemma
	padj.greek_pos = 'METOXI_PP'
	padj.feed(html)

	if not padj.detected:
		if 'ντας' in title:
			wword(title, lemma, 'VERB', greek_pos='METOXI_EE', aspect='Imp', verbform='Conv', voice='Act')
		else:
			wword(title, lemma, 'VERB', greek_pos='METOXI', tags='Incomplete')
	conn.commit()
	print()

for title in adj:
	if form_exists(title, 'ADJ'):
		continue
	padj = AdjParser()
	print('parsing %s:' % title, end='')
	page = get_page(title)
	html = page.html
	sygritikos = r"title=\"συγκριτικός\">συγκριτικός</a> βαθμός του <i><a href=\"/wiki/.*?\" title=\".*?\">(?P<lemma>[ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩαβγδεζηθικλμνξοπρστυφχψωςάέήίόύώΐΰϋϊἱΆΈΉΊΌΎΏΫΪ]+)</a>"
	syg = re.search(sygritikos, html, re.UNICODE)
	if syg is not None:
		print(' συγκριτικός: ' + syg.group("lemma"), end='')
		title = syg.group("lemma")
		padj.degree = "Cmp"

	uperthetikos = r"title=\"υπερθετικός\">υπερθετικός</a> βαθμός του<i> <a href=\"/wiki/.*?\" title=\".*?\">(?P<lemma>[ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩαβγδεζηθικλμνξοπρστυφχψωςάέήίόύώΐΰϋϊἱΆΈΉΊΌΎΏΫΪ]+)</a>"
	sup = re.search(uperthetikos, html, re.UNICODE)
	if sup is not None:
		print(' υπερθετικός: ' + sup.group("lemma"), end='')
		title = sup.group("lemma")
		padj.degree = "Sup"

	padj.lemma = title
	padj.part = 'ADJ'
	padj.feed(html)
	if not padj.detected:
		print('[[' + title + ']]', file=NotDetectedAdj)
		wword(title, title, 'ADJ', tags='Incomplete')
	conn.commit()
	print()

def id_add(string, tag):
	if tag not in string:
		if string != '':
			string += ' '
		string += tag
	return string

for title in nouns:
	if form_exists(title, 'NOUN') or form_exists(title, 'PROPN'):
		continue
	print('parsing %s:' % title, end='')
	page = get_page(title)
	html = page.html

	categories = page.categories
	part = 'NOUN'
	tag = ''
	# Αν ο τίτλος έχει παραπάνω από μία λέξεις βάλε PolyTerm
	for c in categories:
		if c == 'Κατηγορία:Κύρια ονόματα (νέα ελληνικά)':
			part = 'PROPN'
	for c in categories:
		if c == 'Κατηγορία:Πολυλεκτικοί όροι (νεα ελληνικά)':
			tag = id_add(tag, 'PolyTerm')
		if c == 'Κατηγορία:Πόλεις της Ελλάδας (ελληνικά)':
			tag = id_add(tag, 'Top')
			tag = id_add(tag, 'City')
			tag = id_add(tag, 'Greece')
		if c == 'Κατηγορία:Ευρωπαϊκές πρωτεύουσες (ελληνικά)':
			tag = id_add(tag, 'Top')
			tag = id_add(tag, 'Capital')
			tag = id_add(tag, 'Europe')
		if c in ['Κατηγορία:Γυναικεία ονόματα (νέα ελληνικά)', 'Κατηγορία:Ανδρικά ονόματα (νέα ελληνικά)']:
			tag = id_add(tag, 'Ant')
		if c == 'Κατηγορία:Χώρες (ελληνικά)':
			tag = id_add(tag, 'Top')
			tag = id_add(tag, 'Country')
		if c == 'Κατηγορία:Ευρωπαϊκή Ένωση (ελληνικά)':
			tag = id_add(tag, 'Top')
			tag = id_add(tag, 'Top')
			tag = id_add(tag, 'EuropeanUnion')
		if c == 'Κατηγορία:Χημικά στοιχεία (ελληνικά)':
			tag = id_add(tag, 'Element')
		if c == 'Κατηγορία:Πληροφορική_(ελληνικά)':
			tag = id_add(tag, 'Informatics')

	parse_noun(html, title, part, tag)
	conn.commit()
	print()

for word in prs:
	if form_exists(word, 'PRON'):
		continue
	wword(word, word, 'PRON')

for word in advs:
	if form_exists(word, 'ADV'):
		continue
	wword(word, word, 'ADV')

for word in protheseis:
	if form_exists(word, 'ADP'):
		continue
	wword(word, word, 'ADP')

for word in moria:
	if form_exists(word, 'PART'):
		continue
	wword(word, word, 'PART')

for word in epifonimata:
	if form_exists(word, 'INTJ'):
		continue
	wword(word, word, 'INTJ')

# we assume noun as in UD_GREEK
for word in acr:
	if form_exists(word, 'NOUN'):
		continue
	wword(word, word, 'NOUN', tags='Abbr')

# Αριθμητικά
# TODO τακτικά κτλ
for title in num:
	if form_exists(title, 'NUM'):
		continue
	padj = AdjParser()
	print('parsing %s:' % title, end='')
	page = get_page(title)
	html = page.html
	padj.lemma = title
	padj.part = 'NUM'
	padj.feed(html)
	if not padj.detected:
		wword(title, title, 'NUM')
	print()
	conn.commit()

conn.commit()
