import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

y = range(1,4)
x = range(2)

fig = plt.figure(figsize=(10, 8))
outer = gridspec.GridSpec(3, 2, wspace=0.2, hspace=0.2)

for i in range(6):
    inner = gridspec.GridSpecFromSubplotSpec(2, 1,
                    subplot_spec=outer[i], wspace=0.1, hspace=0.1)
    
    for j in range(2):
        ax = plt.Subplot(fig, inner[j])
        t = ax.text(0.5,0.5, 'outer=%d, inner=%d' % (i,j))
        t.set_ha('center')
        ax.set_xticks([])
        ax.set_yticks([])
        fig.add_subplot(ax)

plt.savefig('01')
plt.show()
