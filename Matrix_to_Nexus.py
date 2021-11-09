import os
import sys

"""
Running:

To run this programme you must have a commar deliminated matrix of NxM size with all elements filled such as:

,Isolate1,Isolate2,Isolate3,Isolate4,Isolate5,Isolate6,Isolate7
Gene1,1,1,0,0,0,0,1
Gene2,1,1,1,1,1,0,0
Gene3,1,1,1,1,1,0,0
Gene4,1,1,0,0,0,0,1
Gene5,1,1,1,1,1,0,0
Gene6,1,1,1,1,0,0,0

The programme will build a matrix comparing the column headers too the row headers.

To implement please use

python3 CodeName Input_file.csv Output_file.txt

The output file will be generated in nexus format and can then be read using phylogenetic building software such as splitstree 


"""

Input = open(sys.argv[1]).read().split("\n")
Labels = Input[0].split(",")[1:]


half_matrix = []

alt_Input = []

for line in Input[1:]:
	Line = line.split(",")[1:]
	if len(Line) > 1:
		alt_Input.append(Line)




pos = 0
Complete_Matrix = []
while pos < len(alt_Input[0]):
	values = []
	

	pos2 = 0
	while pos2 < len(alt_Input[0]):
		value = 0
		for line in alt_Input:
			if line[pos] != line[pos2]:
				value = value + 1
		pos2 = pos2 + 1
		values.append(str(value))
	Complete_Matrix.append(values)

	pos = pos + 1

half_matrix = []

i = 1
for line in Complete_Matrix:
	half_matrix.append(line[:i])
	

	i = i + 1


Output = open(sys.argv[2],"w")

Output.write("#NEXUS\n[Distance matrix calculated by BIGSdb Genome Comparator (Mon Nov  8 12:33:15 2021)]\n[Jolley & Maiden 2010 BMC Bioinformatics 11:595]\n[Incomplete loci are ignored in pairwise comparisons unless locus is missing in one isolate]\n\n\nBEGIN taxa;\n   DIMENSIONS ntax = " + str(len(Labels)) + ";\n\nEND;\n\nBEGIN distances;\n   DIMENSIONS ntax = " + str(len(Labels)) + ";\n   FORMAT\n      triangle=LOWER\n      diagonal\n      labels\n      missing=?\n   ;\nMATRIX\n")


i = 0
for l in half_matrix:
	Output.write(Labels[i] + "\t" + "\t".join(l) + "\n")
	i = i + 1

Output.write("   ;\nEND;")

Output.close()



















