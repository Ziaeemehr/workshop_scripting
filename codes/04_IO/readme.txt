As other folks have mentioned, for a really large file, you're better off iterating.

However, you do commonly want the entire thing in memory for various reasons.

genfromtxt is much less efficient than loadtxt (though it handles missing data, whereas loadtxt is more "lean and mean", which is why the two functions co-exist).

If your data is very regular (e.g. just simple delimited rows of all the same type), you can also improve on either by using numpy.fromiter.

If you have enough ram, consider using np.loadtxt('yourfile.txt', delimiter=',') (You may also need to specify skiprows if you have a header on the file.)

As a quick comparison, loading ~500MB text file with loadtxt uses ~900MB of ram at peak usage, while loading the same file with genfromtxt uses ~2.5GB.

Loadtxt Memory and CPU usage of numpy.loadtxt while loading a ~500MB ascii file

Genfromtxt Memory and CPU usage of numpy.genfromtxt while loading a ~500MB ascii file

Alternately, consider something like the following. It will only work for very simple, 
regular data, but it's quite fast. (loadtxt and genfromtxt do a lot of guessing and error-checking.
If your data is very simple and regular, you can improve on them greatly.)
