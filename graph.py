import pickle
from pylab import *
from matplotlib import lines

# open the file and read the data
file = open("data.pickle",'r')
data = pickle.load(file)
file.close()

x = data['x']
y = data['y']
a = data['slope']
b = data['intercept']
r = data['correlation']

print 'The slope : ',a
print 'The intercept : ',b
print 'The correlation coefficient : ',r

# drow graph_
fig = figure()
ax=fig.add_subplot(111)
# scattergram
sc = ax.scatter(x,y,s=25,marker='x', color='b')
# linear regression
func = lambda x: a*x+b
l = lines.Line2D([0,-b/a],[func(0),func(-b/a)], color='r')
ax.add_line(l)
# title
ax.set_title('Linear regression',size=16)
ax.set_xlabel('Engine size',size=14)
ax.set_ylabel('The average miles per gallon',size=14)
show()
