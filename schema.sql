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

CREATE TABLE IF NOT EXISTS related(
	lemma TEXT,
	rel TEXT
);

CREATE TABLE IF NOT EXISTS etymology(
	lemma TEXT,
	rel TEXT
);
