import json
from pprint import pprint
from textblob import TextBlob
import nltk
import csv
import re
from fuzzywuzzy import fuzz

is_noun = lambda pos: pos[:2] == 'NN'
                # do the nlp stuff
tokenized = nltk.word_tokenize('Garlic cloves')
nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
ingredient_name_noun = " ".join(nouns)
ingredient_name_noun = "rice"
# print(ingredient_name_noun)
#
max_similarity = 0
similarity = fuzz.partial_ratio(ingredient_name_noun,"Rice")
print(similarity)
