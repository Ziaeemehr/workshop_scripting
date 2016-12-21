$ sudo aptitude install kcachegrind python-setuptools
$ sudo easy_install -U pyprof2calltree


# profiling:
$ python -m cProfile -o myscript.cprof myscript.py
$ pyprof2calltree -k -i myscript.cprof
