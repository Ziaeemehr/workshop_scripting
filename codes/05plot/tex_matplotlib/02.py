from pylab import figure, text, scatter, show

f = figure()
ax = f.add_subplot(111)
scatter([3,5,2,6,8],[5,3,2,1,5])
ax.text(0.5, 0.5,'matplotlib1',
    horizontalalignment='center',
    verticalalignment='center',
    transform = ax.transAxes)

text(0.1, 0.9,'matplotlib2', 
    ha='center', 
    va='center', 
    transform=ax.transAxes)
show()