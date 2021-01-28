from sys import path
path.insert(0, '..\Interview Questions\Helper')
from mutliplyhelper import multiply
from subtracthelper import subtract
from help.addhelper import add

if __name__ == '__main__':

    mutiple_two_number  = multiply(1,2)
    subtract_two_number = subtract(1,2)
    add_two_number = add(1,2)
    print (mutiple_two_number)
    print(subtract_two_number)
    print(add_two_number)