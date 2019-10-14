#to run 
#cd ./Desktop/
#python 3.7 networkmaker.py

file = open("s2r2G.txt","r")
networkfileforM2 = open("2species2reactionnetworksforM2.txt","w")
networkfile = open("2species2reactionnetworks.txt","w")

for line in file:
	#string = input("Enter string ")
	#s = string.split()
	#s = list(map(int,s))
	s = line.split()
	s = list(map(int,s))
	#print(s)

	reactionverts = range(0,s[0]-1)
	speciesverts = range(s[0],s[0]+s[1]-1)

	#arrows involving reaction vertex 0
	out0 = list([s[i] , s[i+1]] for i in range(2,len(s),2) if s[i]==0 )
	in0 = list([s[i] , s[i+1]] for i in range(2,len(s),2) if s[i+1]==0 )

	#arrows involving reaction vertex 1
	out1 = list([s[i] , s[i+1]] for i in range(2,len(s),2) if s[i]==1 )
	in1 = list([s[i] , s[i+1]] for i in range(2,len(s),2) if s[i+1]==1 )

	#making reaction0
	sourcecomplex0 = list(str(in0[j][0]) for j in range(0,len(in0)))
	sourcecomplex0 = "+".join(sourcecomplex0)

	targetcomplex0 = list(str(out0[j][1]) for j in range(0,len(out0)))
	targetcomplex0 = "+".join(targetcomplex0)

	if not sourcecomplex0:
		sourcecomplex0 = "".join([str(0)])

	if not targetcomplex0:
		targetcomplex0 = "".join([str(0)])

	#print(sourcecomplex0)
	#print(targetcomplex0)

	reaction0 = sourcecomplex0 + "-->" + targetcomplex0
	reaction0 = reaction0.replace('2','A').replace('3','B')
	#print(reaction0)

	#making reaction1
	sourcecomplex1 = list(str(in1[j][0]) for j in range(0,len(in1)))
	sourcecomplex1 = "+".join(sourcecomplex1)

	targetcomplex1 = list(str(out1[j][1]) for j in range(0,len(out1)))
	targetcomplex1 = "+".join(targetcomplex1)

	if not sourcecomplex1:
		sourcecomplex1 = "".join([str(0)])

	if not targetcomplex1:
		targetcomplex1 = "".join([str(0)])

	reaction1 = sourcecomplex1 + "-->" + targetcomplex1
	reaction1 = reaction1.replace('2','A').replace('3','B')
	#print(reaction1)
	
	networkforM2 = "{\"" + reaction0 + "\" , \"" + reaction1 + "\"}," + " NullSymbol => \"0\""
	#print(network)
	networkfileforM2.write(networkforM2 + "\n")

	network = reaction0 + " , " + reaction1
	#print(network)
	networkfile.write(network + "\n")

networkfileforM2.close()
networkfile.close()