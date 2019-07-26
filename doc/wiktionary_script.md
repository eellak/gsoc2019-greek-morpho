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
