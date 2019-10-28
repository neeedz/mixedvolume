#This script will convert the list of reaction networks
#with exactly 2 species and 2 reactions that are formatted as integer strings like "22030312"
#into a list of reaction networks in two formats: (1) that can be used as input into
#Macaulay2 for 'mixed volume' computations, and (2) that looks like a 'traditional'
#presentation of chemical reaction networks, like "A+B->B".
#To run the script, open a terminal window,
#be sure to navigate to the folder where you have the input file "s2r2G.txt" saved
#and then execute the script.
#For example, if the file is saved on the desktop, use the following commands:
#cd ./Desktop/
#python 3.7 NetworkGenerator.py
#The output files "2species2reactionnetworksforM2.txt" and "2species2reactionnetworks.txt"
#will be saved to the current folder.

file = open("s2r2G.txt","r")
networkfileforM2 = open("2species2reactionnetworksforM2.txt","w")
networkfile = open("2species2reactionnetworks.txt","w")

for line in file:
    #convert each line in the input file to a integer string
    s = line.split()
    s = list(map(int,s))

    #The string s can be written as
    #s = #rxn-verts #species-verts source-1 target-1 source-2 target-2 ... source-n target-n
    #For this script, we are only dealing with reactions that have 2 species and 2 reactions
    #The number of reaction vertices is s[0]
    #The number of species vertices is s[1]
    
    #Each consecutive pair of integers in s corresponds to a source species followed by a target species
    #This function makereaction() takes as input a string s and an integer i
    #and outputs all reactions that have species i as an input or as an output.
    def makereaction(s,i):
        #determines which species are in the target complex of the reaction involving species i
        targetspecies = list([s[j] , s[j+1]] for j in range(2,len(s),2) if s[j]==i )
        #determines which species are in the source complex of the reaction involving species i
        sourcespecies = list([s[j] , s[j+1]] for j in range(2,len(s),2) if s[j+1]==i )
        
        sourcecomplex = list(str(sourcespecies[j][0]) for j in range(0,len(sourcespecies)))
        sourcecomplex = "+".join(sourcecomplex)
            
        targetcomplex = list(str(targetspecies[j][1]) for j in range(0,len(targetspecies)))
        targetcomplex = "+".join(targetcomplex)
            
        #if there is no source species, write 0 for the source complex
        if not sourcecomplex:
            sourcecomplex = "".join([str(0)])
        #if there is no target species, write 0 for the target complex
        if not targetcomplex:
            targetcomplex = "".join([str(0)])
            
        #format the reactions; want an arrow between the source complex and the target complex
        #and want to use A to denote the first species and B to denote the second species
        reaction = sourcecomplex + "-->" + targetcomplex
        reaction = reaction.replace('2','A').replace('3','B')
        return reaction;
    
    networkforM2 = "{\"" + makereaction(s,0) + "\" , \"" + makereaction(s,1) + "\"}," + " NullSymbol => \"0\""
    networkfileforM2.write(networkforM2 + "\n")
    
    network = makereaction(s,0) + " , " + makereaction(s,1)
    networkfile.write(network + "\n")

networkfileforM2.close()
networkfile.close()
