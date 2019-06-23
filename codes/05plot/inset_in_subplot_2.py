import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import InsetPosition

fig, ax= plt.subplots()

iax = plt.axes([0, 0, 1, 2], label='iax')
ip = InsetPosition(ax, [0.4, 0.5, 0.2, 0.2]) #posx, posy, width, height
iax.set_axes_locator(ip)
iax.plot([1,2,4])

iax1 = plt.axes([0, 0, 1, 2], label='iax1')
ip = InsetPosition(ax, [0.7, 0.2, 0.2, 0.2]) #posx, posy, width, height
iax1.set_axes_locator(ip)
iax1.plot([1,2,4])


plt.savefig('fig/inset2')
# plt.show()
from sys import exit 
exit(0)

import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import InsetPosition

fig, ax= plt.subplots()

iax = fig.add_axes([0, 0, 1, 2], label="iax")
ip = InsetPosition(ax, [0.4, 0.5, 0.2, 0.2]) #posx, posy, width, height
iax.set_axes_locator(ip)
iax.plot([1,2,4])

iax1 = fig.add_axes([0, 0, 1, 2], label="iax1")
ip = InsetPosition(ax, [0.7, 0.2, 0.2, 0.2]) #posx, posy, width, height
iax1.set_axes_locator(ip)
iax1.plot([1,2,4])

plt.show()