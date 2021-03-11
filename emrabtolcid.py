"""
# This script was written for a sample plot of the alignment data with R because the files with the identity values were one-dimensional (only y-axis i.e. identity values). 

# Goes through the file with IDs and assigns a count to each, then writes that in a new file to make a plot
filename = "D:/Phoenix/R/RScripts/Rtut/emrabtolcidentity_35blast.txt"
newfilename = "D:/Phoenix/R/RScripts/Rtut/modemrabtolcid_35blast.txt"
lcount = 0
with open(filename) as inputfile:
    with open(newfilename, 'w') as outputfile:
        for line in inputfile:
            if lcount == 0:
                outputfile.write('Count Identity\n')
            lcount += 1
            words = line.split()
            outputfile.write(f'{lcount} {words[1]}\n')
"""

# Goes only through the file with one protein (emrab-tolc)
filename = "D:/Phoenix/R/RScripts/Rtut/tolcidentity_35blast.txt"
newfilename = "D:/Phoenix/R/RScripts/Rtut/modtolcid_35blast.txt"
lcount = 0
with open(filename) as inputfile:
    with open(newfilename, 'w') as outputfile:
        for line in inputfile:
            if lcount == 0:
                outputfile.write('Count Identity\n')
            lcount += 1
            words = line.split()
            outputfile.write(f'{lcount} {words[1]}\n')
