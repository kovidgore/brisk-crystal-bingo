# -*- coding: utf-8 -*-
"""Assignment L1- Tokenization_2018IMT-036.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1K0wPWKHELOa2m3TFKRXUilp9_02ylJHL

# Assignment L1 Tokenization

### Name- Harsh walia
### Roll no.-  2018IMT-036

**Problem Statement-**  Use the NLTK Toolkit for demonstrating the Word Tokenization and Sentence Tokenization text pre-processing techniques in NLP.
"""

!pip install --user -U nltk

import nltk
nltk.download('punkt')

from nltk.tokenize import word_tokenize 

text = """Hello My Name is Harsh walia. I am currently pursuing Integrated Btech+Mtech from IIITM Gwalior. I am learning the NLP Course by Professor Debanjan Sadhya"""

word_tokens=word_tokenize(text)
print(word_tokens)

from nltk.tokenize import sent_tokenize

sent_tokens=sent_tokenize(text)
print(sent_tokens)

