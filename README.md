# Matrix_to_Nexus


To run this programme you must have a commar deliminated matrix of NxM size with all elements filled such as:

the cell at 1x1 is expected to hold no value or any title, it is not used in the process of filling the new matrix.

,Isolate1,Isolate2,Isolate3,Isolate4,Isolate5,Isolate6,Isolate7

Gene1,1,1,0,0,0,0,1

Gene2,1,1,1,1,1,0,0

Gene3,1,1,1,1,1,0,0

Gene4,1,1,0,0,0,0,1

Gene5,1,1,1,1,1,0,0

Gene6,1,1,1,1,0,0,0

The programme will build a matrix comparing the column headers too the row headers.

To implement please use:

python3 CodeName Input_file.csv Output_file.txt

The output file will be generated in nexus format and can then be read using phylogenetic building software such as splitstree.
