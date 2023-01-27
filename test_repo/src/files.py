'''
Created on Dec 1, 2022

@author: jcp
'''
print("Module name:\t", __name__, '\n')
import json   

if __name__ == '__main__':
    
    # 10-1. 
    # Write a program that reads the file pi_digits.txt in 'txt files' folder and prints what is in it three times. 
    # Print the contents:
    #    . once by reading in the entire file,
    #    . once by looping over the file object
    #    . once by storing the lines in a list and then working with them outside the with block.
    print("\n\t\t------- Exercise 10.1 ----------\n")
    filename = 'txt files/pi_digits.txt'
    
    #Reads the entire file ... 'with' keyword, python closes the file automatically
    #once outside the with block 
    with open(filename) as file_object:
        entire_file = file_object.read()
    
    print("Reading the file entirely ...")
    print(entire_file)
    
    print("Reading/Printing the file line by line ...")
    with open(filename) as file_object:
        for line in file_object:
            print(line.rstrip())      #Removes the EOL from the line read 
    
    print("Reading the file line by line and printing it outside the with block...")
    with open(filename) as file_object:
        lines = file_object.readlines()
    
    for line in lines:
        print(line.rstrip())
    
    # 10.2
    # Write a program that reads the file pi_million_digits.txt in 'txt files' folder and 
    # finds out if your birthday is in it 
    print("\n\t\t------- Exercise 10.2 ----------\n")
    filename = 'txt files/pi_million_digits.txt'
    
    with open(filename) as file_object:
        lines = file_object.readlines()
    
    pi_string = ""
    for line in lines:
        pi_string += line.strip()           #Removes any spaces and EOL frm the lines read
        
    birthday = input("Enter your birthday in the form ddmmyy:\t")
    if birthday in pi_string:
        print("your birthday is in the first million digits of PI")
    else:
        print("Looser!!! ... Your birthday is not in the first million digits of PI")
        
    print("\n")
    
    #====================File writing ===========================================
    # 10-3. Guest: 
    # . Write a program that prompts the user for their name.
    # . write their name to a file called guest.txt.
    print("\n\t\t------- Exercise 10.3 ----------\n")
    filename = "txt files/guest.txt"
    
    name = input("Enter your name (first name first):\t")
    
    # Writing to the file (open in 'w' mode
    with open(filename, 'w') as file_object:
        file_object.write(name.lower())
    
    # 10-4. Guest Book: Write a while loop that prompts users for their name. When
    # they enter their name, print a greeting to the screen and add a line recording
    # their visit in a file called guest_book.txt. Make sure each entry appears on a
    # new line in the file.
    print("\n\t\t------- Exercise 10.4 ----------\n")
    
    filename = "txt files/guest_book.txt"
    name = ''
    
    with open(filename, 'a') as file_object:
        while True:
            name = input("Enter your name (first name first) or q to terminate:\t")
            name = name.lower()
            if name != 'q':
                print("Welcome in the guest_book", name.title())
                file_object.write('\n' + name.lower())
            else:
                break
    
    # 10-5. Programming Poll: Write a while loop that asks people why they like
    # programming. Each time someone enters a reason, add their reason to a file
    # that stores all the responses.
    print("\n\t\t------- Exercise 10.5 ----------\n")
    
    filename = "txt files/programming_poll.txt"
    
    with open(filename, 'a') as file_object:
        while True:
            poll = input("Why do you like programming (q to Quit):\t")
            if poll != 'q':
                file_object.write('\n' + poll)
            else:
                break
    
    # 10-6. Addition: One common problem when prompting for numerical input occurs when people provide text instead of numbers.
    # When you try to convert the input to an int, you’ll get a ValueError.
    # . Write a program that prompts for two numbers. Add them together and print the result. 
    # . Catch the ValueError if either input value is not a number, and print a friendly error message.
    # . Test your program by entering two numbers and then by entering some text instead of a number.
    # 10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop so the user can continue entering numbers 
    # even if they make a mistake and enter text instead of a number.
    print("\n\t\t------- Exercise 10.6 and 10.7----------\n")
    print("This test makes 2-numbers addition")
    while True:
        n1 = input("Enter your first number:\t")
        n2 = input("Enter your second number:\t")
        try:
            n1 = int(n1)
        except ValueError:
            print('Sorry,', n1, 'is not a number')
        else:
            try:
                n2 = int(n2)
            except ValueError:
                print('Sorry,', n2, 'is not a number')
            else:
                print("Somme = ", n1+n2)
                break
    
    # 10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three names of cats in the first file
    # and three names of dogs in the second file.
    # . Write a program that tries to read these files and print the contents of the file to the screen.
    # . Wrap your code in a try-except block to catch the FileNotFound error, and print a friendly message if a file is missing.
    # . Move one of the files to a different location on your system, and make sure the code in the except block executes properly.
    print("\n\t\t------- Exercise 10.8 ----------\n")
    fcats = "txt files/cats.txt"
    fdogs = "txt files/dogs.txt"
    
    try:
        with open(fcats) as file_object:
            cats = file_object.read()
    except FileNotFoundError:
        print("Cant't Find your cats ...")   
    else: 
        print("---- Your cats ----\n", cats)
        
    try:
        with open(fdogs) as file_object:
            dogs = file_object.read()
    except FileNotFoundError:
        print("Can't find your dogs ...")
    else:    
        print("\n---- Your dogs---- \n", dogs)
    
    # 10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail silently if either file is missing.
    print("\n\t\t------- Exercise 10.9 ----------\n")
    
    try:
        with open(fcats) as file_object:
            cats = file_object.read()
    except FileNotFoundError:
        pass   
    else: 
        print("---- Your cats ----\n", cats)
        
    try:
        with open(fdogs) as file_object:
            dogs = file_object.read()
    except FileNotFoundError:
        pass
    else:    
        print("\n---- Your dogs---- \n", dogs)
    
# JSON and data storing
def json_to_store(filename, data_to_store):
    with open(filename, 'w') as f:
        json.dump(data_to_store, f)   
        
def json_from_store(filename):
    try:
        with open(filename) as f:
            return json.load(f)
    except FileNotFoundError:
        return None
        
def greet_user():
    filename = 'txt files/test.json'
    data = json_from_store(filename)
    if data:
        print('Welcome back', data.title())
    else:
        name = input('Enter your name: ')
        json_to_store(filename, name)
        print('Hi', name.title(), 'I will remember you next time ...')

    
