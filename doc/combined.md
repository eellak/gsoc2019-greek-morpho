---
documentclass: extarticle
mainfont: DejaVu Sans
fontsize: 13pt
geometry: margin=1in
papersize: a4
title: "Documentation for the GSOC 2019"
author: 
- "Konstantinos Agiannis"
---

# Quickstart

## USAGE

Using SQLite3

```
sqlite3 dict.db < dict.sql
```

or

```
sqlite3 dict.db
```

and then

```
.read dict.sql
```

### SQLite3 installation

```
debian/ubuntu
apt install sqlite3
```

### Other DBMS

For a GUI you can use [sqlitebrowser](https://sqlitebrowser.org/)

For any other SQL DBMS (PostgreSQL, MySQL) use the appropriate commands for the import


## SOURCE CODE

[GitHub Repository](https://github.com/eellak/gsoc2019-greek-morpho)

## LICENSE

Copyright (C) 2019, Konstantinos Agiannis

This dictionary is licensed under [Creative Commons Attribution-ShareAlike 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

It contains data extracted from [el.wiktionary.org](https://el.wiktionary.org) licensed under the same license.

# Possible use cases

## Lemmatizing dictionary

A lemmatizing dictionary is one of the most important liguistic resources necessary for NLP.
For Greek there is none available open source one. Using this dictionary is easy to create
one with an SQL query available in the examples.

## Other liguistic resources

### Thessaurus (synonyms)

It contains about 18500 synonyms for various languages. 12500 of which are for Greek.

### Antonyms

It contains about 5500 antonyms, 4300 of which are for Greek.

### Translations

The Database contains almost 150000 translations, from Greek to various languages.
For more translations to Greek or different language pairs,
it is better to check DBnary which has parsed translations from many more wiktionaries.

### Definitions, Etymologies

The database contains parsed definitions and etymologies for most lemmas.



# Database schema

The database contains information according to the following descriptions.

```sql
CREATE TABLE IF NOT EXISTS words(
	form TEXT NOT NULL,
	lemma TEXT NOT NULL,
	pos TEXT NOT NULL,
	greek_pos TEXT,
	gender TEXT,
	ptosi TEXT,
	number TEXT,
	person NUM,
	tense TEXT,
	aspect TEXT,
	mood TEXT,
	verbform TEXT,
	voice TEXT,
	definite TEXT,
	degree TEXT,
	prontype TEXT,
	poss TEXT,
	tags TEXT,
	freq INT
);

CREATE TABLE IF NOT EXISTS def(
	lemma TEXT,
	def TEXT
);

CREATE TABLE IF NOT EXISTS synonyms(
	lemma TEXT,
	syn TEXT
);

CREATE TABLE IF NOT EXISTS antonyms(
	lemma TEXT,
	anton TEXT
);

CREATE TABLE IF NOT EXISTS related(
	lemma TEXT,
	rel TEXT
);

CREATE TABLE IF NOT EXISTS etymology(
	lemma TEXT,
	etym TEXT
);

CREATE TABLE IF NOT EXISTS norm(
	lemma TEXT,
	norm TEXT
);

CREATE TABLE IF NOT EXISTS translations(
	src TEXT NOT NULL,
	src_lemma TEXT NOT NULL,
	dest TEXT NOT NULL,
	dest_lemma TEXT NOT NULL,
	sense TEXT
);

CREATE INDEX IF NOT EXISTS form_index ON words(form);
```

Data is described according to Universal Dependencies. Because tags for verbs are very complicated, an additional attribute greek\_pos was added that simplifies pos information. Because case is a reserved word, the greek word ptosi was used instead.

The attribute tags contains additional *space seperated* information described as follows:

* **Ant**: Anthroponym
* **Top**: Toponym
* **City**, **Country**, **Europe**, **Greece**, **EuropeanUnion**, **Informatics**: Self explained
* **Element**: Chemical Element
* **PolyTerm**: Term composed of multiple words
* **Incomplete**: No inflection table or gender(for nouns) found


# Example queries

## Creation of a table based lemmatizer

This query creates a lemmatizer with the following properties

* form != lemma
* It is a function. There are no two rows with same form and different lemmas 
* Performs normalisation. επτά -> εφτά

```sql
WITH lookup AS 
    (SELECT DISTINCT T1.form,T2.lemma FROM ((SELECT form,lemma FROM words) AS T1  
  INNER JOIN 
    (SELECT form, lemma FROM words UNION SELECT lemma , norm FROM norm) AS T2 
  ON T1.lemma = T2.form) 
    WHERE T1.form != T2.lemma)
SELECT form , lemma FROM lookup 
	WHERE form IN (SELECT form FROM lookup GROUP BY form HAVING count(form) = 1);
```

## All female name forms

```sql
SELECT count(DISTINCT form) FROM words WHERE tags like '%Ant%' AND gender = 'Fem';
```

# Creating the morphological dictionary

## Prerequisites

First python3 and pip3 should be installed in your working environment

The you must install pymediawiki package using

```
pip3 install pymediawiki
```

In some OSes (like freebsd) it may be necessary to install the python3 SQLite3 package

## Running the script

In order to run the script for a small testing subset of the lemmas you run

```
python3 getpages.py
```

To run for all the lemmas you execute

```
python3 getpages.py --production
```

**NOTICE:** Creating the whole dictionary is a very time consuming process.
It takes about 2 days during which you must have a stable internet connection.
If the script stops for various reasons you re-run it. It will automatically continue
from the point it stopped.

## Running on the wiktionary dump

In order to include synonyms,antonyms,normalizations and translations to the database
you must first download the latest el.wiktionary xml dump from [here](https://dumps.wikimedia.org/elwiktionary/latest/elwiktionary-latest-pages-articles-multistream.xml.bz2).

After you extract it, you run

```
python3 parse_dump.py path_to_wiktionary_xml path_to_dict.db
```

**NOTICE:** Running this script requires about 4.5 GB of free RAM.
# Instructions for creating a word list suitable for a spelling dictionary

The most important factor for a good spelling dictionary is the quality of
the texts used. As more text sources are used, spelling errors are accumulated
in the final dictionary.

## Pipeline

Stages

1. *(optional)* text preprocess script depending on the type of the text

2. a tokenizer outputting result as one word per line
(only greek words without puctuation or symbols). For this task
we use the tokenizer found in fast-tokenizer submodule.
If a line contains a decimal number after the word, it is assumed that
the number is the frequency of the word. This is useful when spelling
dictionaries with frequency information are concatenated.

3. word\_post\_process.py script that removes common spelling errors and
outputs a dictionary with frequency information

## Example usage

Dictionary for Greek Wikipedia dump with frequency information

```
bzcat wiki.dump.bz2 | ftok -a greek | python3 word_post_process.py --min-freq 2 > dict.dic
```

*ftok -a greek* performs tokenization of the text from stdin and outputs
to stdout only greek words

As Wikipedia contains many spelling errors, we include words having frequency at least 2

It is advised to use text sources with better spelling quality than Wikipedia


# Future improvements

## Morphological dictionary

The morphological dictionary found in this repo contains information
found in el.wiktionary.org. Thus the best way to contribute, is to add
inflection tables in el.wiktionary.org for lemmas that don't have one.
You can about the articles' stucture [**here**](https://el.wiktionary.org/wiki/%CE%92%CE%B9%CE%BA%CE%B9%CE%BB%CE%B5%CE%BE%CE%B9%CE%BA%CF%8C:%CE%94%CE%BF%CE%BC%CE%AE_%CF%84%CF%89%CE%BD_%CE%AC%CF%81%CE%B8%CF%81%CF%89%CE%BD) and a list of inflection templates [**here**](https://el.wiktionary.org/wiki/%CE%9A%CE%B1%CF%84%CE%B7%CE%B3%CE%BF%CF%81%CE%AF%CE%B1:%CE%A0%CF%81%CF%8C%CF%84%CF%85%CF%80%CE%B1_%CE%BA%CE%BB%CE%AF%CF%83%CE%B5%CF%89%CE%BD_(%CE%B5%CE%BB%CE%BB%CE%B7%CE%BD%CE%B9%CE%BA%CE%AC)).

