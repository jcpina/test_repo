'''
A simple program illustrating Loops

Created on Nov 12, 2022

@author: jcp
'''
if __name__ == '__main__':
    pass

print("Module name:\t", __name__, '\n')    

# from loops import looping
# from functions import calculator
from files import greet_user
from time import sleep

def wait_and_clear_console():
    lines = 5
    sleep(5)
    while lines != 0:
        print(" ")
        lines = lines - 1

# looping()
# wait_and_clear_console()
#
# calculator()
# wait_and_clear_console()

#Greet the user and remember him for the next time (JSON file)
greet_user()

print("\t\t\t\tThat's all folks ...")
