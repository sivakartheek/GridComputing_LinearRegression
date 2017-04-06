import pickle
import math

file = open("04cars.dat", 'r')

x = []
y = []
xy = []
x2 = []
y2 = []
n=0

# read the data and create lists
for line in file:
    lineList = line
    data = list(lineList)
    if ("*" in data) == False:
        size = float(data[74] + data[75] + data[76])
        highway = float(data[88] + data[89])
        city = float(data[85] + data[86])
        mpg = 0.5*(highway + city)
        x.append(size)
        y.append(mpg)
        xy.append(size*mpg)
        x2.append(size*size)
        y2.append(mpg*mpg)
        n += 1
file.close()

# the values needed to calculate
sumX = sum(x)
sumY = sum(y)
sumXY = sum(xy)
sumXSquared = sum(x2)
sumYSquared = sum(y2)

# calculate the slope and intercept
slope = (n*sumXY - sumX*sumY) / (n*sumXSquared - sumX*sumX)
intercept = (sumY - slope*sumX) / n

# calculate the correlation
r1 = n*sumXY - sumX*sumY
r2 = n*sumXSquared - sumX*sumX
r3 = n*sumYSquared - sumY*sumY
correlation = r1 / math.sqrt(r2*r3)

# create the output object
out = {'x':x, 'y':y, 'slope':slope, 'intercept':intercept, 'correlation':correlation}

# write in the file
file = open("data.pickle",'w')
pickle.dump(out, file)
file.close()


