# The factory pattern comes under the creational patterns list category. It provides one of the best ways to create an object. In factory pattern, objects are created without exposing the logic to client and referring to the newly created object using a common interface. Factory patterns are implemented in Python using factory method. When a user calls a method such that we pass in a string and the return value as a new object is implemented through factory method. The type of object used in factory method is determined by string which is passed through method. In the example below, every method includes object as a parameter, which is implemented through factory method.


class Button(object):
    html = ""

    def get_html(self):
        return self.html


class Image(Button):
    html = "<img><\img>"


class Input(Button):
    html = "<input></input>"


class Flash(Button):
    html = "<obj></obj>"


class ButtonFactory():
    def create_button(self, typ):
        targetclass = typ.capitalize()
        return globals()[targetclass]()


button_obj = ButtonFactory()
buttons = ["image", "input", "flash"]

for b in buttons:
    print (button_obj.create_button(b).get_html())
