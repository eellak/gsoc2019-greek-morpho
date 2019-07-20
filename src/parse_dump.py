from xml.etree import ElementTree as ET
import sys
import re
import sqlite3

if len(sys.argv) != 3:
	sys.exit('ERROR: Usage\n%s Wiktionary_Dump SQLite3_Database' % sys.argv[0])

tree = ET.parse(sys.argv[1])
root = tree.getroot()
ns = 'http://www.mediawiki.org/xml/export-0.10/'

conn = sqlite3.connect(sys.argv[2])
cur = conn.cursor()

def parse_translations(code, title):
	for a in re.finditer(r"{{μτφ-αρχή\|?(?P<SENSE>[^}]*?)}}(?P<MTF>.*?)({{μτφ-τέλος}}|{{κλείδα-ελλ}})", code, re.DOTALL|re.UNICODE):
		for b in re.finditer(r"{{τ\|(?P<LANG>[a-z]{2,3})\|(?P<TRANSLATION>[^|]+?)(\||}).*?}", a.group('MTF'), re.UNICODE):
			if b.group('TRANSLATION') in ['ΧΧΧ', 'XXX']:# both greek and english characters
				continue
			cur.execute("INSERT INTO translations VALUES(?,?,?,?,?)",
			('el', title, b.group('LANG'), b.group('TRANSLATION'), a.group('SENSE')))


def parse_normalisation(code, title):
	a = re.search(r"{{γραφή του ?\|(?P<NORM>[^}|]+)", code, re.UNICODE)
	if a is not None:
		cur.execute("INSERT INTO norm VALUES(?,?)", (title, a.group('NORM')))

def parse_synonyms(code, title):
	for a in re.finditer(r"{{συνων(\|[^}]+)?}}(?P<SYN>.+)", code, re.UNICODE):
		for b in re.finditer(r"(^\s*|,\s*)\[\[(?P<SYN>[^\]|]+)(\|[^\]\[]+)?\]\](?=(\s*$|\s*,))", a.group('SYN'), re.UNICODE):
			cur.execute("INSERT INTO synonyms VALUES(?,?)", (title, b.group('SYN')))

	syn_list = re.search(r"==={{συνώνυμα}}====*(?P<SYN_LIST>[^=]+)(?=\=\=)", code, re.UNICODE | re.DOTALL)
	if syn_list is not None:
		for a in re.finditer(r"\*\s*\[\[(?P<SYN>[^\]\[|]+)(\|[^\]]+)?\]\]\s*$", syn_list.group('SYN_LIST'), re.UNICODE):
			cur.execute("INSERT INTO synonyms VALUES(?,?)", (title, a.group('SYN')))


def parse_antonyms(code, title):
	for a in re.finditer(r"{{αντων(\|[^}]+)?}}(?P<ANTON>.+)", code, re.UNICODE):
		for b in re.finditer(r"(^\s*|,\s*)\[\[(?P<ANTON>[^\]|]+)(\|[^\]\[]+)?\]\](?=(\s*$|\s*,))", a.group('ANTON'), re.UNICODE):
			cur.execute("INSERT INTO antonyms VALUES(?,?)", (title, b.group('ANTON')))

	antonym_list = re.search(r"==={{αντώνυμα}}====*(?P<ANTON_LIST>[^=]+)(?=\=\=)", code, re.UNICODE | re.DOTALL)
	if antonym_list is not None:
		for a in re.finditer(r"\*\s*\[\[(?P<ANTON>[^\]\[|]+)(\|[^\]]+)?\]\]\s*$", antonym_list.group('ANTON_LIST'), re.UNICODE):
			cur.execute("INSERT INTO antonyms VALUES(?,?)", (title, a.group('ANTON')))

def parse_related(code, title):
	related_list = re.search(r"==={{συγγενικά}}====*(?P<REL_LIST>[^=]+)(?=\=\=)", code, re.UNICODE | re.DOTALL)
	if related_list is not None:
		for a in re.finditer(r"\*\s*\[\[(?P<REL>[^\]\[|]+)(\|[^\]]+)?\]\]\s*$", related_list.group('REL_LIST'), re.UNICODE):
			cur.execute("INSERT INTO related VALUES(?,?)", (title, a.group('REL')))

for page in root.findall('{%s}page' % ns):
	title = page.find('{%s}title' % ns).text
	namespace = page.find('{%s}ns' % ns).text
	revision = page.find('{%s}revision' % ns)
	code = revision.find('{%s}text' % ns).text

	if code is not None and namespace == '0':
		parse_translations(code, title)
		parse_normalisation(code, title)
		parse_synonyms(code, title)
		parse_antonyms(code, title)
		parse_related(code, title)

conn.commit()
