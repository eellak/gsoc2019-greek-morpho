# Instructions for creating a word list suitable for a spelling dictionary

The most important factor for a good spelling dictionary is the quality of
the texts used. As more text sources are used, spelling errors are accumulated
in the final dictionary.

## Pipeline

Stages

1. *(optional)* text preprocess script depending on the type of the text

2. a tokenizer outputting result as one word per line
(only greek words without puctuation or symbols). For this
we use the tokenizer found in fast-tokenizer submodule.
If a line contains a decimal number after the word, it is assumed that
the number is the frequency of the word. This is useful when spelling
dictionaries with frequency information are concatenated.

3. word\_post\_process.py script that removes common spelling errors and
outputs a dictionary with frequency information

## Example usage

Dictionary for Greek Wikipedia dump with frequency information

```
bzcat wiki.dump | ftok -a greek | python3 word_post_process.py --min-freq 2 > dict.dic
```

*ftok -a greek* performs tokenization of the text from stdin and outputs
to stdout only greek words

As Wikipedia contains many spelling errors here we include words having frequency at least 2

It is advised to use text sources with better spelling quality than Wikipedia


