# Join Words into a Sentence
from functools import reduce
text = ["Python", "is", "awesome"]
result= reduce(lambda x,y :x + " "+y,text)
print (result)

