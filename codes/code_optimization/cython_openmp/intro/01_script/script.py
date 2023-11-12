# Cython compilation for developers

import pyximport
pyximport.install()
# pyximport.install(pyimport=True)

import hello 
hello.say_hello_to("World")
