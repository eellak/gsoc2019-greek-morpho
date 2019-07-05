from xml.etree import ElementTree as ET
import sys
import re

if len(sys.argv) != 2:
	sys.exit('ERROR: please give xml dump')

tree = ET.parse(sys.argv[1])
root = tree.getroot()
ns = 'http://www.mediawiki.org/xml/export-0.10/'


def parse_translations(code, title):
	for a in re.finditer(r"{{μτφ-αρχή\|?(?P<CASE>[^}]*?)}}(?P<MTF>.*?)({{μτφ-τέλος}}|{{κλείδα-ελλ}})", code, re.DOTALL|re.UNICODE):
		# TODO υπάρχουν και άλλες επιλογές πχ iw= link=
		for b in re.finditer(r"{{τ\|(?P<LANG>[a-z]{2,3})\|(?P<TRANSLATION>[^|]+?)(\||}).*?}", a.group('MTF'), re.UNICODE):
			if b.group('TRANSLATION') in ['ΧΧΧ', 'XXX']:# both greek and english characters
				continue

			print("%s:%s:%s:%s" % (title, b.group('LANG'), b.group('TRANSLATION'), a.group('CASE')))


def parse_normalisation(code, title):
	for a in re.finditer(r"{{γραφή του ?\|(?P<NORM>[^}|]+)", code, re.DOTALL|re.UNICODE):
		print("NORM %s:%s" % (title, a.group('NORM')))


for page in root.findall('{%s}page' % ns):
	title = page.find('{%s}title' % ns).text
	namespace = page.find('{%s}ns' % ns).text
	revision = page.find('{%s}revision' % ns)
	code = revision.find('{%s}text' % ns).text

	if code is not None and namespace == '0':
		parse_translations(code, title)
		parse_normalisation(code, title)
