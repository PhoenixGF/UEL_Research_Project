"""K-means clustering"""
# unsupervised learning technique - converging on clusters of data
# how to choose clusters? start low, keep increasing k as until standard error stops decreasing

from numpy import array

idlist = []
numlist = []
ncount = 0
comlist = []
with open('Data/emraidentity35.txt') as inputfile:
    for line in inputfile:
        ncount += 1
        line = line.strip()
        line = float(line)
        idlist += [line]
        numlist += [ncount]
        comlist += [[ncount, line]]

print(idlist)
print(numlist)
print(comlist)

data = array(comlist)
print(data)

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from numpy import float

model = KMeans(n_clusters=10)  # you wouldn't know this value in reality

# Scaling to make data comparable
model = model.fit(scale(data))

##  We can look at the clusters each data point was assigned to
print(model.labels_)

##  And we'll visualize it:
plt.figure(figsize=(8,6))
plt.scatter(data[:,0], data[:,1], c=model.labels_.astype(float))
plt.show()
