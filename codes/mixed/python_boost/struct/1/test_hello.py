import hello
planet = hello.World(2.,5.)  #when constructor added this does not work
# planet = hello.World("howdy")
planet.set('howdy')
print planet.greet()