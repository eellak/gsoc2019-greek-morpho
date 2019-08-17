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
	src\_lemma TEXT NOT NULL,
	dest TEXT NOT NULL,
	dest\_lemma TEXT NOT NULL,
	sense TEXT
);

CREATE INDEX IF NOT EXISTS form\_indes ON words(form);
```

Data is described according to Universal Dependencies. Because tags for verbs are very complicated, an additional attribute greek\_pos was added that simplifies pos information. Because case is a reserved word, the greek word ptosi was used instead.

The attribute tags contains additional *space seperated* information described as follows:

* **Ant**: Anthroponym
* **Top**: Toponym
* **City**, **Country**, **Europe**, **Greece**, **EuropeanUnion**, **Informatics**: Self explained
* **Element**: Chemical Element
* **PolyTerm**: Term composed of multiple words
* **Incomplete**: No inflection table or gender(for nouns) found

