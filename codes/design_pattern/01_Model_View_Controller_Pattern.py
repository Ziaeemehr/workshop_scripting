# Model View Controller Pattern

import json
# --------------------------------------------------------#
# model.py


class Person(object):

    def __init__(self, first_name=None, last_name=None):

        self.first_name = first_name
        self.last_name = last_name
        # returns Person name, ex: John Doe

    def name(self):
        return ("%s %s" % (self.first_name, self.last_name))

    @classmethod
    def getAll(cls):
        # returns all people inside db.txt as list of Person objects

        database = open('db.json', 'r')
        result = []
        json_list = json.load(database)
        for item in json_list:
            person = Person(item['first_name'], item['last_name'])
            result.append(person)
        return result


# --------------------------------------------------------#
# view.py
# View never interacts with model. controller does this work
# (communicating with model and view).

def showAllView(list):
    print ('In our db we have %i users. Here they are:' % len(list))
    for item in list:
        print (item.name())


def startView():
    print ('MVC - the simplest example')
    print ('Do you want to see everyone in my db?[y/n]')


def endView():
    print ('Goodbye!')
# --------------------------------------------------------#
# controller.py
# Controller interacts with model through the getAll() method
# which fetches all the records displayed to the end user.

def showAll():
    # gets list of all Person objects
    people_in_db = Person.getAll()
    # calls view
    return showAllView(people_in_db)


def start():
    startView()
    _input = input()
    if _input == 'y':
        return showAll()
    else:
        return endView()

# --------------------------------------------------------#


if __name__ == "__main__":
    # running controller function
    start()
