
# Version 1
# Parses a file with seqIDs and extracts sequences from corresponding database in the form of a fasta file,
# writing the output in a separate fasta file

import time

infilename = input('Please type the full path to the input file with seqIDs, delineated by forward slash, '
                   'for exapmple D:/Phoenix/Documents Microsoft/...emrabtolcsaccver_blast.txt\nFile: ')
# D:/Phoenix/Documents Microsoft/UEL BS/Level 6/Research Project/Summaries/BLAST/blast-2.11.0+/db/emrabtolcexcelsaccver190121.txt

indatabase = input('Please type the full path to the input database folder\nFile: ')
# D:/Phoenix/Documents Microsoft/UEL BS/Level 6/Research Project/Summaries/BLAST/blast-2.11.0+/db/newcombined.fasta

outfilename = input('Please type the full path to the output file in which to save all the sequences\nFile: ')
# D:/Phoenix/Documents Microsoft/UEL BS/Level 6/Research Project/Summaries/BLAST/blast-2.11.0+/db/parsedseqs.fasta

start = time.time()
with open(outfilename, 'w') as outputfile:
    with open(infilename) as inputfile:
            for saccver in inputfile:
                saccver = saccver.strip()
                # print(saccver)
                with open(indatabase) as f:
                    ifile = iter(f)
                    for line in f:
                        if saccver in line:
                            # print('in line, writing')
                            outputfile.write(line)
                            line = next(ifile)
                            while '>' not in line:
                                # print('writing seqs')
                                outputfile.write(line)
                                line = next(ifile)
                            break

end = time.time()
print(end-start)