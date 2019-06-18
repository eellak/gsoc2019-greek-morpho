# GSOC 2019 - Development of a Greek open source Morphological dictionary and application of it to Greek spelling tools

## Dictionary Download

The version v0.1 of the dictionary can be found [here](http://snf-869216.vm.okeanos.grnet.gr/dict.zip)

It contains almost 500000 distinct surface forms and about 900000 forms with morphological information. 

### How to open

After installing sqlite3(,zip)

```
debian/ubuntu
apt install sqlite3 zip
```

Then run

```
unzip dict.zip
sqlite3 dict.db
```

You can now use SQL
```sql
SELECT form,lemma FROM words WHERE form != lemma LIMIT 100;
```

## Running the script

### Dependencies

```
pip3 install pymediawiki
```

### Run Testing

```
python3 getpages.py
```

### Run production

```
python3 getpages.py production
```

## Project goals

During the summer a Morphological dictionary in sqlite3 format will be created.
Information will be extracted automatically with a python script and using
the pymediawiki library. In addition words and morphological information
will be added to the spelling tool dictionaries.

## Deliverables

1. A Morphological dictionary of Greek in SQLite3 format that includes complete morphology for 
 Nouns, Proper Nouns, Adjectives, Verbs, Prepositions, Adverbs, Acronyms
 with information automatically extracted from the Greek wiktionary
 using Universal Dependencies Tagset.
2. Addition of the extracted words and POS to open source Greek Spelling
 dictionaries and rules based on POS will be written.

## Timeline

### Phase 1 (May 27 - Jun 28)

Creation of a parsing tool for Greek wiktionary that parses nouns, adjectives, verbs using Universal Dependencies POS tags

### Phase 2 Phase 2 (Jun 29 - Jul 26)

Addition of remaining parts of speech to the Morphological dictionary and
 addition of further information tags like toponyms and terminology extracted from page categories.

### Phase 3 (Jul 27 - Aug 26)

 Addition of extracted surface forms to Greek spelling dictionaries including words from reliable sources like European parliament translations.

## Contributors

* Google summer of code participant: Konstantinos Agiannis
* Mentor: Kostas Papadimas
* Mentor: Diomidis Spinellis
* Mentor: Alexios Zavras


## License

The source code is under GPLv3.

The produced database with the morphological dictionary is under [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

## Links

 * [Greek Wiktionary](https://el.wiktionary.org/)
 * [hunspell documentation](https://www.systutorials.com/docs/linux/man/4-hunspell/)
 * [UD\_GREEK-GDT](https://github.com/UniversalDependencies/UD_Greek-GDT/)
 * [Tagset Greek](http://nlp.ilsp.gr/nlp/tagset_examples/tagset_el/)
 * [Fast Tokenizer](https://github.com/algorithm314/fast-tokenizer)
