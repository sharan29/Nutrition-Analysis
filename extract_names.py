import json
from pprint import pprint
from textblob import TextBlob
import nltk
import csv
import re
from fuzzywuzzy import fuzz

def getName():
    f = open('name1.txt', "r")
    f1 = open('final_recipeIDs.txt',"w+")
    lines = list(f)

    a=set();
    for line in lines:
        str=""
        for i in range(len(line)-7,0,-1):
            #print(i)
            if(line[i]!='_'):
                str=str+line[i];
            else:
                break;
        str=str[::-1];
        # print(str)
        # a.add(int(str))
        f1.write(str)
        f1.write("\n")
        # print(int(str))
    return a
# getName()

def extract_diff():
    f1 = open("downloadThisRecipies_try.txt","w+")
    f = open("remaining.txt")
    lines = list(f)
    f = open("final_recipeIDs.txt")
    lines1 = list(f)
    l3 = [x for x in lines if x not in lines1]
    # print(len(l3))
    for value in l3:
        f1.write(value[:-1])
        f1.write("\n")
        # print (value[:-2])
# extract_diff()

def getIngredientsSet():
    f = open('recipenames.txt', "r")
    f1 = open('AllIngredients-only-nouns_set.txt','w+')
    lines = list(f)
    itemsSet = set()
    i1=0;
    for line in lines:
        # f1 = open('All_Items/'+line,'r')
        with open('All_Items/'+line[:-1]) as f:
            data = json.load(f)
            for i in data['Ingredients']:
                # itemsSet.add(i['Name'])
                # print(i['Name'])
                # blob = TextBlob(i['Name'])
                # print(i['Name'],blob.noun_phrases)
                if i['Name'] == None:
                    continue
                is_noun = lambda pos: pos[:2] == 'NN'
                # do the nlp stuff
                tokenized = nltk.word_tokenize(i['Name'])
                nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
                # print(i['Name'])
                # print(i['Name'],nouns)
                k = " ".join(nouns)
                itemsSet.add(k)
                # f1.write(k)
                # f1.write("\n")

                # print(i['Name'])
                i1+=1
    for i in itemsSet:
        f1.write(i)
        f1.write("\n")
    print(len(itemsSet),i1)
    return itemsSet
getIngredientsSet()

class Item:
    def __init__(self, item_name,code):
        self.item_name=item_name
        self.code = code

def readIfctDataset():
    itemsDict = dict()
    f1 = open("items_database_2.txt",'w+')
    with open('try.csv','r') as csvfile:
        lines = csv.reader(csvfile,delimiter=',')
        for row in lines:
            if(re.search('[A-Z][0-9]{3}',row[1])):
                item_name = row[2]
                code = row[1]
                item = Item(item_name,code)
                itemsDict[item_name] = code
    all_ingredients = getIngredientsSet()
    for i in all_ingredients:
        for key in itemsDict.keys():
            l = key.split(",")[0]            
            max_similarity = 0
            similarity = fuzz.partial_ratio(i,l)
            # for j in l:
                
            #     if max_similarity < similarity:
            #         max_similarity = similarity
            if(similarity > 80):
                f1.write(i+"--->"+key)
                f1.write("\n")
# readIfctDataset()
