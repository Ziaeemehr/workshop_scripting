import pylab as pl
import numpy as np
from bidi.algorithm import get_display
import arabic_reshaper


def make_farsi_text(string):
    reshaped_text = arabic_reshaper.reshape(string)
    farsi_text = get_display(reshaped_text)
    return farsi_text


xlabel = "برچسب محور افقی"
ylabel = "برچسب محور عمودی"
title = "عنوان نمودار"
font_title = {'family': 'B Titr',
              'color': 'red',
              'weight': 'normal',
              'size': 30,
              }
font_labels = {'family': 'B Nazanin',
               'color': 'black',
               'weight': 'normal',
               'size': 20,
               }

x = np.random.rand(20)

pl.plot(x, "ko")
pl.xlabel(make_farsi_text(xlabel), fontdict=font_labels)
pl.ylabel(make_farsi_text(ylabel), fontdict=font_labels)
pl.title(make_farsi_text(title), fontdict=font_title)
pl.tight_layout()
pl.savefig("fig.png")
pl.show()
