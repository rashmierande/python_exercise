'''
Please plot the data of this file into a graph of x and y axis.
'''

#Answer 1
import pandas
import pylab as plt

# data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
# data.plot(x='x', y='y', kind='scatter')
# plt.show()

# This solution uses the pylab library which needs
# to be installed with pip install pylab . The solution
# has few lines of code and uses the integrated pandas plot method.
# Instead of scatter , you can specify other types of plots
# such as line , bar , etc.

from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

output_file("bokeh_plot.html")
data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
f = figure()
f.circle(x=data["x"], y=data["y"])

show(f)

#This solution uses the Bokeh library which needs to be
# installed with pip install bokeh . In contrast to Pylab,
# Bokeh produces web based visualizations. In this example
# we are plotting the data as circles, but other geometries
# can be used such as line , triangle , etc.