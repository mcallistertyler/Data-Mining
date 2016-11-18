#print stuff into terminal first because i'm shit at doing the code thing
from random import shuffle
from sys import argv
g = open("optallshuffle.arff", "w")
listof = []
number_of_fields = 64


g.write("@RELATION optallshuffle")
g.write("\n")
g.write("\n")
for x in range(1, number_of_fields+1):
  g.write("@ATTRIBUTE p")
  g.write(str(x))
  g.write(" NUMERIC ")
  g.write("\n")
g.write("\n")
g.write("@ATTRIBUTE class" + "{0,1,2,3,4,5,6,7,8,9}")
g.write("\n")
g.write("@DATA")
g.write("\n")
with open("optall.txt") as f:
    for line in f:
    	numbers_str = line.split()
    	numbers_float = [int(x) for x in numbers_str]
    	listof.append(numbers_float)
shuffle(listof)
for x in range(0, len(listof)):
	g.write(", ".join(str(e) for e in listof[x]))
	g.write("\n")
g.close()
