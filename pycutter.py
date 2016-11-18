from sys import argv
g = open("optallcutinhalf.arff", "w")
listof = []
number_of_fields = 65
with open("optall.txt") as f:
	for line, t in enumerate(f):
		length = line + 1
		halflength = length / 2
	f.close()
g.write("@RELATION optall")
g.write("\n")
g.write("\n")
for x in range(1, number_of_fields):
  g.write("@ATTRIBUTE p")
  g.write(str(x))
  g.write(" NUMERIC ")
  g.write("\n")
g.write("\n")
g.write("@ATTRIBUTE class" + "{0,1,2,3,4,5,6,7,8,9}")
g.write("\n")
g.write("@DATA")
g.write("\n")
count = 0
with open("optall.txt") as f:
	for line in f:
		count = count + 1
		numbers_str = line.split()
		numbers_float = [int(x) for x in numbers_str]
		g.write(", ".join(str(e) for e in numbers_float))
		g.write("\n")
		if count == halflength:
			break
	g.close()