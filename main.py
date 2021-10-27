# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from fileinput import filename


def print_hi(name, f_h=None):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    def greet_user():
        """Display a simple greeting"""
        print('harel')

    greet_user()

    # creating a dog class:
    # Creating a dog class
    class Dog():
        """Represent a dog"""

        def __init__(self, name):
            """Initialize dog object"""
            self.name = name

        def sit(self):
            """Simulate sitting"""
            print(self.name + " is sitting.")
            print(self)

    # how to use Dog(name) e.g. Dog('Peso')
    my_dog = Dog('Peso')

    print(my_dog.name + " is a great dog!")
    my_dog.sit()

    # Inheritance

    class SARDog(Dog):
        """represent a search dog."""

        def __init__(self, name):
            """Initialize the sardog"""
            super().__init__(name)

        def search(self):
            """Simulate searching."""
            print(self.name + " is searching")
            print(self)

    my_dog = SARDog('Willie')

    print(my_dog.name + "is a search dog.")
    my_dog.sit()
    my_dog.search()

    # fh = open('demo.txt', 'w')
    # for i in range(10):
    #     fh.write("this is the line no %d\n" % i)
    #
    # fh.close()
    #
    # # Reading a file and storing its lines
    #
    # filename = 'demo.txt'
    #
    # with open(filename) as file_object:
    #     lines = file_object.readlines()
    #
    # for line in lines:
    #     print(line)
    #
    #
    # # Writing to a file
    # filename = 'journal.txt'
    # with open(filename, 'w') as file_object:
    #     file_object.write("I love programing.")
    #
    # # Appending to a file
    # filename = 'journal.txt'
    # with open(filename, 'a') as file_object:
    #     file_object.write("\nI love making games")

    # promt ="how many tickets do you need?"
    # num_tickets=input(promt)
    #
    # try:
    #     num_tickets=int(num_tickets)
    # except ValueError:
    #     print("Please try again.")
    # else:
    #     print("your tickets is printing!")

    # users = ['val', 'bob', 'mia', 'ron', 'ned']
    # users.sort()
    #
    # for number in range(-51, 40):
    #     print(number)
    #
    # numbers = list(range(1, 1000))
    # print("len is:" + len(numbers))

import matplotlib.pyplot as plt

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
