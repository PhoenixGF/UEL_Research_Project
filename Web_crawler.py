import time
import requests
import bs4

start = time.time()
filename = "D:/Phoenix/Documents Microsoft/UEL BS/Level 6/Research Project/" \
           "Summaries/BLAST/blast-2.11.0+/files/Species names.txt"

"""
# Version 1, searches in Pubmed using species name (first two words in each line of the file if line is not empty) 
with open(filename) as f:
    for line in f:
        line = line.strip()
        if line != '':
            splist = line.split()
            if len(splist) > 1:
                urlsearch1 = splist[0] + '+' + splist[1]
                # urlsearch2 = splist[0]
                # print(urlsearch1)
            else:
                urlsearch1 = splist[0]
                
        res = requests.get(f'https://pubmed.ncbi.nlm.nih.gov/?term=EmrB+{urlsearch1}')
        res.raise_for_status()
        tastysoup = bs4.BeautifulSoup(res.text, features="html.parser")
        delicioussoup = str(tastysoup)
        if 'No results were found' in delicioussoup:
            print('No results were found', urlsearch1)
        else:
            print(urlsearch1)
"""
"""
# Version 2, searches in Pubmed only using the genus name (the first word in each line of the species name file) 

protname = input('Please provide the name of the protein to search for\nProtein: ')

with open(f'D:/Phoenix/Documents Microsoft/UEL BS/Level 6/Research Project/'
          f'Summaries/BLAST/blast-2.11.0+/files/Pubmed search {protname}.txt', 'w') as outputfile:
    with open(filename) as f:
        flist = []
        for line in f:
            line = line.strip()
            if line != '':
                splist = line.split()
                if splist[0] not in flist:
                    urlsearch2 = splist[0]
                    flist += [urlsearch2]
                else:
                    continue

                res = requests.get(f'https://pubmed.ncbi.nlm.nih.gov/?term={protname}+{urlsearch2}')
                res.raise_for_status()
                tastysoup = bs4.BeautifulSoup(res.text, features="html.parser")
                delicioussoup = str(tastysoup)
                if 'No results were found' in delicioussoup:
                    print('No results were found', urlsearch2)
                else:
                    print(urlsearch2)
                    outputfile.write(f'{urlsearch2}\n')
"""


# Searches in Google Scholar like version 2, but this time also writes the hits to a file automatically
with open("D:/Phoenix/Documents Microsoft/UEL BS/Level 6/Research Project/"
          "Summaries/BLAST/blast-2.11.0+/files/GScholar search.txt", 'w') as outputfile:
    with open(filename) as f:
        flist = []
        for line in f:
            line = line.strip()
            if line != '':
                splist = line.split()
                if splist[0] not in flist:
                    urlsearch2 = splist[0]
                    flist += [urlsearch2]
                else:
                    continue

                res = requests.get(f'https://scholar.google.co.uk/'
                                   f'scholar?hl=en&as_sdt=0%2C5&as_ylo=2020&q=EmrB+{urlsearch2}&btnG=')
                res.raise_for_status()
                tastysoup = bs4.BeautifulSoup(res.text, features="html.parser")
                delicioussoup = str(tastysoup)
                if 'did not match' in delicioussoup:
                    print('No results were found', urlsearch2)
                else:
                    print(urlsearch2)
                    outputfile.write(f'{urlsearch2}\n')
                time.sleep(120.0)

end = time.time()
print('Time taken in seconds:', end-start)


"""
# Code for checking
res = requests.get(f'https://scholar.google.co.uk/scholar?hl=en&as_sdt=0%2C5&q=EmrB+AM6&btnG=')
res.raise_for_status()
tastysoup = bs4.BeautifulSoup(res.text, features="html.parser")
delicioussoup = str(tastysoup)
print(delicioussoup)
if 'did not match' in delicioussoup:
    print('No results were found')
"""


# print(type(tastysoup))
# print(tastysoup)
# print(type(res))
# print(res.status_code == requests.codes.ok)
# print(len(res.text))
# print(res.text)