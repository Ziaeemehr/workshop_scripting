"""
    Builder Pattern is a unique design pattern which helps in building complex object using simple objects and uses an algorithmic approach. This design pattern comes under the category of creational pattern. In this design pattern, a builder class builds the final object in step-by-step procedure. This builder is independent of other objects.

    !# Advantages of Builder Pattern
        - It provides clear separation and a unique layer between construction and representation of a specified object created by class.
        - It provides better control over construction process of the pattern created.
        - It gives the perfect scenario to change the internal representation of objects.
"""


class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getCar(self):
        car = Car()

        # First goes the body
        body = self.__builder.getBody()
        car.setBody(body)

        # Then engine
        engine = self.__builder.getEngine()
        car.setEngine(engine)

        # And four wheels
        i = 0
        while i < 4:
            wheel = self.__builder.getWheel()
            car.attachWheel(wheel)
            i += 1
        return car

# The whole product


class Car:
    def __init__(self):
        self.__wheels = list()
        self.__engine = None
        self.__body = None

    def setBody(self, body):
        self.__body = body

    def attachWheel(self, wheel):
        self.__wheels.append(wheel)

    def setEngine(self, engine):
        self.__engine = engine

    def specification(self):
        print ("body: %s" % self.__body.shape)
        print ("engine horsepower: %d" % self.__engine.horsepower)
        print ("tire size: %d\'" % self.__wheels[0].size)


class Builder:
    def getWheel(self): pass
    def getEngine(self): pass
    def getBody(self): pass


class JeepBuilder(Builder):

    def getWheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel

    def getEngine(self):
        engine = Engine()
        engine.horsepower = 400
        return engine

    def getBody(self):
        body = Body()
        body.shape = "SUV"
        return body

# Car parts


class Wheel:
    size = None


class Engine:
    horsepower = None


class Body:
    shape = None


def main():
    jeepBuilder = JeepBuilder()  # initializing the class
    
    director = Director()

    # Build Jeep
    print ("Jeep")
    director.setBuilder(jeepBuilder)
    jeep = director.getCar()
    jeep.specification()
    print ("")


if __name__ == "__main__":
    main()
