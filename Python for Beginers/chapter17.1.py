import matplotlib.pyplot as ptl

years = [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008] #x axis
bilion_dollars = [12, 13, 45, 47, 56, 67, 67, 68] #y axis

#plot function receives two arguments (two lists, X and Y) and draws a polygon
ptl.plot(years, bilion_dollars)

#x axis label
ptl.xlabel("Years")

#y axis label
ptl.ylabel("Billion Dollars")

#display the graph
ptl.show()