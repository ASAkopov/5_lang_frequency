# Frequency Analysis of Words

The module returns most frequent words in a text file, in a descending order of their occurence number.

### Using module functions in interactive regime:

Import module:
```python
import lang_frequency as lf
```
Load text from file into a string:
```python
text = lf.load_data(wp1.txt):
```
Get 10 most frequent words from loaded text string:
```python
print(lf.get_most_frequent_words(text, 10))

[('и', 137), ('в', 121), ('на', 72), ('с', 64), ('не', 64), ('что', 44), ('из', 35), ('его', 34), ('о', 32), ('то', 31)]
```
### Using module from command line:
```python
python3 lang_frequency.py wp1.txt 10

[('и', 137), ('в', 121), ('на', 72), ('с', 64), ('не', 64), ('что', 44), ('из', 35), ('его', 34), ('о', 32), ('то', 31)]
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
