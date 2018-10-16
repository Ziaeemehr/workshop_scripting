import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import InsetPosition

fig, ax= plt.subplots()

iax = plt.axes([0, 0, 1, 2])
ip = InsetPosition(ax, [0.4, 0.5, 0.3, 0.7]) #posx, posy, width, height
iax.set_axes_locator(ip)

iax.plot([1,2,4])
plt.show()