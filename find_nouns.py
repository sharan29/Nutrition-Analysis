import json
from pprint import pprint
from textblob import TextBlob
import nltk
import csv
import re
from fuzzywuzzy import fuzz

def readIfctDataset():
    itemsDict = dict()
    with open('try.csv','r') as csvfile:
        lines = csv.reader(csvfile,delimiter=',')
        for row in lines:
            if(re.search('[A-Z][0-9]{3}',row[1])):
                item_name = row[2]
                code = row[1]
                itemsDict[item_name] = code

    return itemsDict

def getIngredientsSet():
    f = open('recipenames.txt', "r")
    f1 = open('map_ingredients_with_ifct_2.txt','w+')
    lines = list(f)
    itemsSet = set()
    i1=0;
    itemsDict = readIfctDataset()
    for line in lines:
        with open('All_Items/'+line[:-1]) as f:
            data = json.load(f)
            f1.write(line)
            for i in data['Ingredients']:
                if i['Name'] == None:
                    continue
                is_noun = lambda pos: pos[:2] == 'NN'
                # do the nlp stuff
                tokenized = nltk.word_tokenize(i['Name'])
                nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
                # ingredient_name_noun = " ".join(nouns)
                max_similarity = 0
                for k1 in nouns:
                    for key in itemsDict.keys():
                    # similarity = fuzz.partial_ratio(ingredient_name_noun,key[:key.find('(')])                    
                        similarity = fuzz.partial_ratio(k1.title(),key[:key.find('(')].split(',')[0])
                        if max_similarity <= similarity:
                            max_similar_key = key
                            max_similarity = similarity
                    if(max_similarity == 100):
                        f1.write(i["Name"]+"---->"+k1+"--->"+max_similar_key)
                        f1.write("\n")
    #              
                    # if(similarity > 60):
                    #     f1.write(i["Name"]+"---->"+ingredient_name_noun+"--->"+key)
                    #     f1.write("\n")
    #             itemsSet.add(ingredient_name_noun)
    #             f1.write(ingredient_name_noun)
    #             f1.write("\n")
    #             i1+=1
    #
    # print(len(itemsSet),i1)
    # return itemsSet

class Item:
    def __init__(self, item_name,code):
        self.item_name=item_name
        self.code = code


getIngredientsSet()
