import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


def make_ticklabels_invisible(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        for tl in ax.get_xticklabels() + ax.get_yticklabels():
            tl.set_visible(False)



# demo 3 : gridspec with subplotpars set.

f = plt.figure(figsize=(10,15))

# plt.suptitle("title")

left1  = 0.05
right1 = 0.48

left2  = 0.55
right2 = 0.98

h = 0.2
dh = 0.02

gs1 = GridSpec(2, 1)
gs1.update(left=left1, right=right1, hspace=0, bottom=3*h+dh, top=1-dh)
ax1_1 = plt.subplot(gs1[0])
ax1_2 = plt.subplot(gs1[1])


gs2 = GridSpec(2, 1)
gs2.update(left=left2, right=right2, hspace=0, bottom=3*h+dh, top=1-dh)
ax2_1 = plt.subplot(gs2[0])
ax2_2 = plt.subplot(gs2[1])

gs3 = GridSpec(2, 1)
gs3.update(left=left1, right=right1, hspace=0.0, bottom=h+dh, top=3*h-dh)
ax3_1 = plt.subplot(gs3[0])
ax3_2 = plt.subplot(gs3[1])

gs4 = GridSpec(2, 1)
gs4.update(left=left2, right=right2, hspace=0.0, bottom=h+dh, top=3*h-dh)
ax4_1 = plt.subplot(gs4[0])
ax4_2 = plt.subplot(gs4[1])

gs5 = GridSpec(1, 1)
gs5.update(left=left1, right=right1, bottom=dh, top=h-dh)
ax5 = plt.subplot(gs5[0])

gs6 = GridSpec(1, 1)
gs6.update(left=left2, right=right2, bottom=dh, top=h-dh)
ax6 = plt.subplot(gs6[0])

# gs2 = GridSpec(3, 3)
# gs2.update(left=0.55, right=0.98, hspace=0.05)
# ax4 = plt.subplot(gs2[:, :-1])
# ax5 = plt.subplot(gs2[:-1, -1])
# ax6 = plt.subplot(gs2[-1, -1])


make_ticklabels_invisible(plt.gcf())
plt.savefig('003')
# plt.show()

