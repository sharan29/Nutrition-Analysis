import re
f1 = open('AllIngredients-only-nouns_set.txt','r')
f2 = open('outliers.txt','w+')
lines = list(f1)
for i in lines:
	result = re.match('^[A-Z ]*$', i)
	if result:
		f2.write(i)
