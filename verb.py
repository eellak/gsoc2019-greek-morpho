import re
import sys
from parse import get_forms,wword,cur,form_exists,esc

energ = """\<center\>\ \Ε\ξ\α\κ\ο\λ\ο\υ\θ\η\τ\ι\κ\ο\ί\ \χ\ρ\ό\ν\ο\ι\ \<\/center\>
\<\/th\>\<\/tr\>
\<tr\>
\<th\>\π\ρ\ό\σ\ω\π\α
\<\/th\>
\<th\>\Ε\ν\ε\σ\τ\ώ\τ\α\ς
\<\/th\>
\<th\>\Π\α\ρ\α\τ\α\τ\ι\κ\ό\ς
\<\/th\>
\<th\>\Ε\ξ\.\ \Μ\έ\λ\λ\.
\<\/th\>
\<th\>\Υ\π\ο\τ\α\κ\τ\ι\κ\ή
\<\/th\>
\<th\>\Π\ρ\ο\σ\τ\α\κ\τ\ι\κ\ή
\<\/th\>
\<th\ align\=\"center\"\>\Μ\ε\τ\ο\χ\ή
\<\/th\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\α\'\ \ε\ν\ι\κ\.
\<\/td\>
\<td\>(?P<ENEST_A_ENIKO>.*?)
\<\/td\>
\<td\>(?P<PARATATIKOS_A_ENIKO>.*?)
\<\/td\>
\<td\>(?P<EX_MEL_A_ENIKO>.*?)
\<\/td\>
\<td\>(?P<YPOT_EX_A_ENIKO>.*?)
\<\/td\>
\<td\>
\<\/td\>
\<td\ rowspan\=\"6\"\ align\=\"center\"\>(?P<METOXI>.*?)
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\β\'\ \ε\ν\ι\κ\.
\<\/td\>
\<td\>(?P<ENEST_B_ENIKO>.*?)
\<\/td\>
\<td\>(?P<PARATATIKOS_B_ENIKO>.*?)
\<\/td\>
\<td\>\θ\α\ (.*?)
\<\/td\>
\<td\>\ν\α\ (.*?)
\<\/td\>
\<td\>(?P<PROST_ENEST_B_ENIKO>.*?)
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\γ\'\ \ε\ν\ι\κ\.
\<\/td\>
\<td\>(?P<ENEST_G_ENIKO>.*?)
\<\/td\>
\<td\>(?P<PARATATIKOS_G_ENIKO>.*?)
\<\/td\>
\<td\>\θ\α\ (.*?)
\<\/td\>
\<td\>\ν\α\ (.*?)
\<\/td\>
\<td\>
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\α\'\ \π\λ\η\θ\.
\<\/td\>
\<td\>(?P<ENEST_A_PL>.*?)
\<\/td\>
\<td\>(?P<PARATATIKOS_A_PL>.*?)
\<\/td\>
\<td\>\θ\α\ (.*?)
\<\/td\>
\<td\>\ν\α\ (.*?)
\<\/td\>
\<td\>
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\β\'\ \π\λ\η\θ\.
\<\/td\>
\<td\>(?P<ENEST_B_PL>.*?)
\<\/td\>
\<td\>(?P<PARATATIKOS_B_PL>.*?)
\<\/td\>
\<td\>\θ\α (.*?)
\<\/td\>
\<td\>\ν\α (.*?)
\<\/td\>
\<td\>(?P<PROST_ENEST_B_PL>.*?)
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\γ\'\ \π\λ\η\θ\.
\<\/td\>
\<td\>(?P<ENEST_G_PL>.*?)
\<\/td\>
\<td\>(?P<PARATATIKOS_G_PL>.*?)
\<\/td\>
\<td\>\θ\α\ (.*?)
\<\/td\>
\<td\>\ν\α\ (.*?)
\<\/td\>
\<td\>
\<\/td\>\<\/tr\>
\<tr\>
\<th\ colspan\=\"7\"\ style\=\"background\:\#e2e4c0\"\>\<center\>\ \Σ\υ\ν\ο\π\τ\ι\κ\ο\ί\ \χ\ρ\ό\ν\ο\ι\ \<\/center\>
\<\/th\>\<\/tr\>
\<tr\>
\<th\>\π\ρ\ό\σ\ω\π\α
\<\/th\>
\<th\>
\<\/th\>
\<th\>\Α\ό\ρ\ι\σ\τ\ο\ς
\<\/th\>
\<th\>\Σ\υ\ν\ο\π\τ\.\ \Μ\έ\λ\λ\.
\<\/th\>
\<th\>\Υ\π\ο\τ\α\κ\τ\ι\κ\ή
\<\/th\>
\<th\>\Π\ρ\ο\σ\τ\α\κ\τ\ι\κ\ή
\<\/th\>
\<th\ align\=\"center\"\>\Α\π\α\ρ\έ\μ\φ\α\τ\ο
\<\/th\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\α\'\ \ε\ν\ι\κ\.
\<\/td\>
\<td\ rowspan\=\"6\"\>
\<\/td\>
\<td\>(?P<AOR_A_ENIKO>.*?)
\<\/td\>
\<td\>\θ\α\ (.*?)
\<\/td\>
\<td\>\ν\α\ (?P<AOR_YPOT_A_ENIKO>.*?)
\<\/td\>
\<td\>
\<\/td\>
\<td\ rowspan\=\"6\"\ align\=\"center\"\>(?P<AOR_APAREMFATO>.*?)
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\β\'\ \ε\ν\ι\κ\.
\<\/td\>
\<td\>(?P<AOR_B_ENIKO>.*?)
\<\/td\>
\<td\>\θ\α\ (.*?)
\<\/td\>
\<td\>\ν\α\ (?P<AOR_YPOT_B_ENIKO>.*?)
\<\/td\>
\<td\>(?P<PROST_AOR_B_ENIKO>.*?)
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\γ\'\ \ε\ν\ι\κ\.
\<\/td\>
\<td\>(?P<AOR_G_ENIKO>.*?)
\<\/td\>
\<td\>\θ\α\ (.*?)
\<\/td\>
\<td\>\ν\α\ (?P<AOR_YPOT_G_ENIKO>.*?)
\<\/td\>
\<td\>
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\α\'\ \π\λ\η\θ\.
\<\/td\>
\<td\>(?P<AOR_A_PL>.*?)
\<\/td\>
\<td\>\θ\α\ (.*?)
\<\/td\>
\<td\>\ν\α\ (?P<AOR_YPOT_A_PL>.*?)
\<\/td\>
\<td\>
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\β\'\ \π\λ\η\θ\.
\<\/td\>
\<td\>(?P<AOR_B_PL>.*?)\
\<\/td\>
\<td\>\θ\α\ (.*?)
\<\/td\>
\<td\>\ν\α\ (?P<AOR_YPOT_B_PL>.*?)
\<\/td\>
\<td\>(?P<PROST_AOR_B_PL>.*?)
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\γ\'\ \π\λ\η\θ\.
\<\/td\>
\<td\>(?P<AOR_G_PL>.*?)
\<\/td\>
\<td\>\θ\α\ (.*?)
\<\/td\>
\<td\>\ν\α\ (?P<AOR_YPOT_G_PL>.*?)
\<\/td\>
\<td\>
\<\/td\>\<\/tr\>
\<tr\>
"""

metoxi = """\<td\ rowspan\=\"6\"\ align\=\"center\"\>\<a\ href\=\"\/wiki\/(.*?)\"\ title\=\"(.*?)\"\>(?P<METOXI2>.*?)\<\/a\>
\<\/td\>"""

mono_exakolouthitikoi = """\<tr\>
\<th\>\π\ρ\ό\σ\ω\π\α
\<\/th\>
\<th\>\Ε\ν\ε\σ\τ\ώ\τ\α\ς
\<\/th\>
\<th\>\Π\α\ρ\α\τ\α\τ\ι\κ\ό\ς
\<\/th\>
\<th\>\Ε\ξ\.\ \Μ\έ\λ\λ\.
\<\/th\>
\<th\>\Υ\π\ο\τ\α\κ\τ\ι\κ\ή
\<\/th\>
\<th\>\Π\ρ\ο\σ\τ\α\κ\τ\ι\κ\ή
\<\/th\>
\<th\ align\=\"center\"\>\Μ\ε\τ\ο\χ\ή
\<\/th\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\α\'\ \ε\ν\ι\κ\.
\<\/td\>
\<td\>(?P<ENEST_A_ENIKO>.*?)
\<\/td\>
\<td\>(?P<PARATATIKOS_A_ENIKO>.*?)
\<\/td\>
\<td\>(?P<EX_MEL_A_ENIKO>.*?)
\<\/td\>
\<td\>(?P<YPOT_EX_A_ENIKO>.*?)
\<\/td\>
\<td\>
\<\/td\>
\<td\ rowspan\=\"6\"\ align\=\"center\"\>(?P<METOXI>.*?)
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\β\'\ \ε\ν\ι\κ\.
\<\/td\>
\<td\>(?P<ENEST_B_ENIKO>.*?)
\<\/td\>
\<td\>(?P<PARATATIKOS_B_ENIKO>.*?)
\<\/td\>
\<td\>\θ\α\ (.*?)
\<\/td\>
\<td\>\ν\α\ (.*?)
\<\/td\>
\<td\>(?P<PROST_ENEST_B_ENIKO>.*?)
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\γ\'\ \ε\ν\ι\κ\.
\<\/td\>
\<td\>(?P<ENEST_G_ENIKO>.*?)
\<\/td\>
\<td\>(?P<PARATATIKOS_G_ENIKO>.*?)
\<\/td\>
\<td\>\θ\α\ (.*?)
\<\/td\>
\<td\>\ν\α\ (.*?)
\<\/td\>
\<td\>
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\α\'\ \π\λ\η\θ\.
\<\/td\>
\<td\>(?P<ENEST_A_PL>.*?)
\<\/td\>
\<td\>(?P<PARATATIKOS_A_PL>.*?)
\<\/td\>
\<td\>\θ\α\ (.*?)
\<\/td\>
\<td\>\ν\α\ (.*?)
\<\/td\>
\<td\>
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\β\'\ \π\λ\η\θ\.
\<\/td\>
\<td\>(?P<ENEST_B_PL>.*?)
\<\/td\>
\<td\>(?P<PARATATIKOS_B_PL>.*?)
\<\/td\>
\<td\>\θ\α (.*?)
\<\/td\>
\<td\>\ν\α (.*?)
\<\/td\>
\<td\>(?P<PROST_ENEST_B_PL>.*?)
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\γ\'\ \π\λ\η\θ\.
\<\/td\>
\<td\>(?P<ENEST_G_PL>.*?)
\<\/td\>
\<td\>(?P<PARATATIKOS_G_PL>.*?)
\<\/td\>
\<td\>\θ\α\ (.*?)
\<\/td\>
\<td\>\ν\α\ (.*?)
\<\/td\>
\<td\>"""

#print(re.sub(r'\\\n','\n',re.escape(t))) # this produces the above

def s(s):
	if s == None:
		return ''
	return s

def add_verb(form,greek_pos,lemma,person,number,tense,mood,aspect,verbform,voice,*args, **kwargs):
	tags = kwargs.get('tags',None)
	all_forms = get_forms(form)
	for i in all_forms:
		#print(i +' '+ lemma + ' ' + str(s(person)) + ' '+s(number)+' '+s(tense)+' '+s(mood)+' '+s(aspect)+' '+s(verbform)+' '+s(voice))
		wword(i,lemma,'VERB',person=person,tags=tags,number=number,tense=tense,mood=mood,aspect=aspect,verbform=verbform,voice=voice,greek_pos=greek_pos)


def parse_verb(html,code,lemma):
	#TODO εντοπισμός {{παθ|}}
	#μετοχές {{μτχππ| και {{μτχπε|
	# TODO μετοχές ούμενος
	v = 'Act'
	res = re.search("\<div class=\"NavHead\" align=\"left\">&#160; &#160; Ενεργητική φωνή</div>",html,re.DOTALL|re.UNICODE)
	if res == None:
		v = 'Pass'
	detected = 0
	for a in re.finditer(energ,html,re.DOTALL|re.UNICODE):
		detected = 1
		if v == 'Pass' and form_exists(a.group('ENEST_A_ENIKO'),'VERB'):#Αν έχουμε βάλει το παθητικό λήμμα
			cur.execute("DELETE FROM words WHERE lemma = \'%s\'"%(esc(a.group('ENEST_A_ENIKO'))))

		if v == 'Pass':
			met = re.search(metoxi,html,re.DOTALL|re.UNICODE)
			if met != None:
				print(' Η μετοχή είναι: ' + met.group('METOXI2'),end='')
				wword(met.group('METOXI2'),lemma,'VERB',greek_pos='METOXI_PP',gender='Masc',ptosi='Nom',number='Sing',aspect='Perf',verbform='Part',voice='Pass',tags='Incomplete')
			else:
				print(' Δεν βρέθηκε μετοχή',end='')
		add_verb(a.group('ENEST_A_ENIKO'),'ENEST_A_ENIKO',lemma,1,'Sing','Pres','Ind','Imp','Fin',v)
		add_verb(a.group('ENEST_B_ENIKO'),'ENEST_B_ENIKO',lemma,2,'Sing','Pres','Ind','Imp','Fin',v)
		add_verb(a.group('ENEST_G_ENIKO'),'ENEST_G_ENIKO',lemma,3,'Sing','Pres','Ind','Imp','Fin',v)
		add_verb(a.group('ENEST_A_PL'),'ENEST_A_PL',lemma,1,'Plur','Pres','Ind','Imp','Fin',v)
		add_verb(a.group('ENEST_B_PL'),'ENEST_B_PL',lemma,2,'Plur','Pres','Ind','Imp','Fin',v)
		add_verb(a.group('ENEST_G_PL'),'ENEST_G_PL',lemma,3,'Plur','Pres','Ind','Imp','Fin',v)

		add_verb(a.group('AOR_A_ENIKO'),'AOR_A_ENIKO',lemma,1,'Sing','Past','Ind','Perf','Fin',v)
		add_verb(a.group('AOR_B_ENIKO'),'AOR_B_ENIKO',lemma,2,'Sing','Past','Ind','Perf','Fin',v)
		add_verb(a.group('AOR_G_ENIKO'),'AOR_G_ENIKO',lemma,3,'Sing','Past','Ind','Perf','Fin',v)
		add_verb(a.group('AOR_A_PL'),'AOR_A_PL',lemma,1,'Plur','Past','Ind','Perf','Fin',v)
		add_verb(a.group('AOR_B_PL'),'AOR_B_PL',lemma,2,'Plur','Past','Ind','Perf','Fin',v)
		add_verb(a.group('AOR_G_PL'),'AOR_G_PL',lemma,3,'Plur','Past','Ind','Perf','Fin',v)

		add_verb(a.group('PARATATIKOS_A_ENIKO'),'PARATATIKOS_A_ENIKO',lemma,1,'Sing','Past','Ind','Imp','Fin',v)
		add_verb(a.group('PARATATIKOS_B_ENIKO'),'PARATATIKOS_B_ENIKO',lemma,2,'Sing','Past','Ind','Imp','Fin',v)
		add_verb(a.group('PARATATIKOS_G_ENIKO'),'PARATATIKOS_G_ENIKO',lemma,3,'Sing','Past','Ind','Imp','Fin',v)
		add_verb(a.group('PARATATIKOS_A_PL'),'PARATATIKOS_A_PL',lemma,1,'Plur','Past','Ind','Imp','Fin',v)
		add_verb(a.group('PARATATIKOS_B_PL'),'PARATATIKOS_B_PL',lemma,2,'Plur','Past','Ind','Imp','Fin',v)
		add_verb(a.group('PARATATIKOS_G_PL'),'PARATATIKOS_G_PL',lemma,3,'Plur','Past','Ind','Imp','Fin',v)

		if v == 'Act':
			add_verb(a.group('METOXI'),'METOXI_EE',lemma,None,None,None,None,'Imp','Conv',v)
		else:
			if a.group('METOXI') not in [None,""]:
				form = re.search('>(?P<MET>.*?)\<\/a\>',a.group('METOXI'),re.UNICODE)
				#print('a.group = ',a.group('METOXI'))
				if form != None:
					wword(form.group('MET'),lemma,'VERB',greek_pos='METOXI_PE',gender='Masc',ptosi='Nom',number='Sing',aspect='Perf',verbform='Part',voice='Pass',tags='Incomplete')
			#add_verb(a.group('METOXI'),'METOXI_PE',lemma,None,None,None,None,'Imp','Conv',v,tags='Incomplete')

		add_verb(a.group('AOR_APAREMFATO'),'AOR_APAREMFATO',lemma,None,None,None,None,'Perf','Inf',v)

		add_verb(a.group('PROST_ENEST_B_ENIKO'),'PROST_ENEST_B_ENIKO',lemma,2,'Sing',None,'Imp','Ind','Fin',v) # Λογικά Ind 
		add_verb(a.group('PROST_ENEST_B_PL'),'PROST_ENEST_B_PL',lemma,2,'Sing',None,'Imp','Ind','Fin',v)

		add_verb(a.group('PROST_AOR_B_ENIKO'),'PROST_AOR_B_ENIKO',lemma,2,'Sing',None,'Imp','Perf','Fin',v)
		add_verb(a.group('PROST_AOR_B_PL'),'PROST_AOR_B_PL',lemma,2,'Sing',None,'Imp','Perf','Fin',v)

		#γιατί οριστική για αυτό;??????
		add_verb(a.group('AOR_YPOT_A_ENIKO'),'AOR_YPOT_A_ENIKO',lemma,1,'Sing',None,'Ind','Perf','Fin',v)
		add_verb(a.group('AOR_YPOT_B_ENIKO'),'AOR_YPOT_B_ENIKO',lemma,2,'Sing',None,'Ind','Perf','Fin',v)
		add_verb(a.group('AOR_YPOT_G_ENIKO'),'AOR_YPOT_G_ENIKO',lemma,3,'Sing',None,'Ind','Perf','Fin',v)
		add_verb(a.group('AOR_YPOT_A_PL'),'AOR_YPOT_A_PL',lemma,1,'Plur',None,'Ind','Perf','Fin',v)
		add_verb(a.group('AOR_YPOT_B_PL'),'AOR_YPOT_B_PL',lemma,2,'Plur',None,'Ind','Perf','Fin',v)
		add_verb(a.group('AOR_YPOT_G_PL'),'AOR_YPOT_G_PL',lemma,3,'Plur',None,'Ind','Perf','Fin',v)
		v = 'Pass'

	v = 'Act'
	a = re.search(mono_exakolouthitikoi,html,re.DOTALL|re.UNICODE)
	if detected == 0 and a != None:
		add_verb(a.group('ENEST_A_ENIKO'),'ENEST_A_ENIKO',lemma,1,'Sing','Pres','Ind','Imp','Fin',v)
		add_verb(a.group('ENEST_B_ENIKO'),'ENEST_B_ENIKO',lemma,2,'Sing','Pres','Ind','Imp','Fin',v)
		add_verb(a.group('ENEST_G_ENIKO'),'ENEST_G_ENIKO',lemma,3,'Sing','Pres','Ind','Imp','Fin',v)
		add_verb(a.group('ENEST_A_PL'),'ENEST_A_PL',lemma,1,'Plur','Pres','Ind','Imp','Fin',v)
		add_verb(a.group('ENEST_B_PL'),'ENEST_B_PL',lemma,2,'Plur','Pres','Ind','Imp','Fin',v)
		add_verb(a.group('ENEST_G_PL'),'ENEST_G_PL',lemma,3,'Plur','Pres','Ind','Imp','Fin',v)
		
		add_verb(a.group('PARATATIKOS_A_ENIKO'),'PARATATIKOS_A_ENIKO',lemma,1,'Sing','Past','Ind','Imp','Fin',v)
		add_verb(a.group('PARATATIKOS_B_ENIKO'),'PARATATIKOS_B_ENIKO',lemma,2,'Sing','Past','Ind','Imp','Fin',v)
		add_verb(a.group('PARATATIKOS_G_ENIKO'),'PARATATIKOS_G_ENIKO',lemma,3,'Sing','Past','Ind','Imp','Fin',v)
		add_verb(a.group('PARATATIKOS_A_PL'),'PARATATIKOS_A_PL',lemma,1,'Plur','Past','Ind','Imp','Fin',v)
		add_verb(a.group('PARATATIKOS_B_PL'),'PARATATIKOS_B_PL',lemma,2,'Plur','Past','Ind','Imp','Fin',v)
		add_verb(a.group('PARATATIKOS_G_PL'),'PARATATIKOS_G_PL',lemma,3,'Plur','Past','Ind','Imp','Fin',v)
		
		add_verb(a.group('PROST_ENEST_B_ENIKO'),'PROST_ENEST_B_ENIKO',lemma,2,'Sing',None,'Imp','Ind','Fin',v) # Λογικά Ind 
		add_verb(a.group('PROST_ENEST_B_PL'),'PROST_ENEST_B_PL',lemma,2,'Sing',None,'Imp','Ind','Fin',v)
		detected = 1;
		
	#ΤODO VerbForm=Conv για τις μετοχές οντας, VerbForm=Inf για τα απαρρέμφατα,VerbForm=Part με Voice=Pass για τις μετομές που προκείπτουν από ρήμα
	#για τις άλλες μετοχές ADJ,VerbForm=Fin για τα άλλα
	
	if detected == 0:
		wword(lemma,lemma,'VERB',tags="Incomplete")


