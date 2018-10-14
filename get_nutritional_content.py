import csv
import json
import json
from pprint import pprint
from textblob import TextBlob
import nltk
import re
from fuzzywuzzy import fuzz

def search_item_name_in_index(item_name):
	fp = open("map1.txt")
	lines = list(fp)
	flag = 0
	for line in lines:
		line1 = line[:line.find(':')].strip(" ")
		if(line1 == item_name):
			flag = 1
			item_codes =line[line.find(":")+1:-1].split(",") 
			print(line1,item_codes)
			
			break
	if flag == 0:
		print(item_name,":Not Found")
recipe_name = input()
with open('./All_Items/'+recipe_name+'.json') as f:
    data = json.load(f)
for i in range(len(data['Ingredients'])):
	item_name = data['Ingredients'][i]['Name']
	is_noun = lambda pos: pos[:2] == 'NN'
	# do the nlp stuff
	tokenized = nltk.word_tokenize(item_name)
	nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
	search_name = " ".join(nouns)
	search_item_name_in_index(search_name)


