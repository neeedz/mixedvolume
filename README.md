# Reformatting network strings for mixed volume computations

We provide a Python script NetworkGenerator.py that will convert the list of reaction networks
with exactly 2 species and 2 reactions that are formatted as integer strings like "22030312"
into a list of reaction networks in two formats: (1) that can be used as input into
Macaulay2 for 'mixed volume' computations, and (2) that looks like a 'traditional'
presentation of chemical reaction networks, like "A+B->B".

To run the script, open a terminal window,
be sure to navigate to the folder where you have the input file "s2r2G.txt" and the script "NetworkGenerator.py" saved
and then execute the script.
For example, if the file is saved on the desktop, use the following commands:

cd ./Desktop/

python3.7 NetworkGenerator.py

The output files "2species2reactionnetworksforM2.txt" and "2species2reactionnetworks.txt"
will be saved to the current folder.

Psuedocode for translating between network string and a network presented in the format for the Macaulay2 package ReactionNetworks.m2

s = #rxn-verts #species-verts source-1 target-1 source-2 target-2 ... source-n target-n

	make a square vertex 0, 1, ..., s[0]-1
	make a circle vertex s[0], s[0]+1, ..., s[0]+s[1]-1
	draw an arrow s[i] -> s[i+1] for each pair s[i] s[i+1] starting from i = 2 until i=len(s)-1 by 2

to retrieve network now

define empty sum to be 0
find square vertex 0

	reaction source = sum of all species pointing in to 0
	reaction target = sum of all species pointing out of 0
	output as "reaction source --> reaction target" (to be used in M2)

in general: find square vertex j
	
	reaction source = sum of all species pointing in to j
	reaction target = sum of all species pointing out of j
	output as rxnj = "reaction source --> reaction target" [a string] (to be used in M2)

do this for all reaction verts j = 0, 1, ... , s[0]-1

then network = {rxn1, ... , rxnm}, NullSymbol => "0"


will then be able to pass to M2 as follows
	
	N = reactionNetwork(network)
	R = createRing(N,QQ)
	steadyStateEquations N
	conservationEquations N
