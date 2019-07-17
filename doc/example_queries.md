# Creation of a table based lemmatizer

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

# All female name forms

```sql
SELECT count(DISTINCT form) FROM words WHERE tags like '%Ant%' AND gender = 'Fem';
```

