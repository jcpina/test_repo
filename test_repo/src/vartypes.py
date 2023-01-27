'''
A simple program illustrating usage of python object types

 Dictionaries, Lists and Tuples
 Lists - Lists of values. Each one has a number, in ascending order and beginning from zero.
         Value can be removed and new ones added in when needed.
 Tuples - Similar to lists but the values cannot change.
 Dictionaries - They include an index of all the words and a definition of each one. Words are called
                keys and the definitions are called values.
                Values are not numbered in dictionaries and they are not in any particular order.
                Keys can be added, removed or changed in a dictionary.

Created on Nov 20, 2022

@author: jcp
'''

def list_basics():
    months = ('January', 'February', 'March', 'April')  #This is a tuple
    cats = ['Smokey', 'Josie', 'Suzy', 'Tom']           #This is a list
    
    print(months)
    print(months[2])
    # cannot do an assigment ... dics are like constants months[2] = "December"

    print("My cat list:\n\t", cats)
    print("\nThe [2] element of my cat list:\n\tt", cats[2])

    cats[2] = "Mimi"
    print("\nReplaced the [2] cat with Mimi:\n\t", cats[2])
    
    print("\nPrinting the entire cat's list using [0:] index:\n\t",cats[0:])
    
    cats.append('Sylvester')
    print("\nAppending Sylvester to my cats:\n\t", cats)
    
    del cats[1]
    print("\nRemoved the cats[1] with the 'del cats[1]:\n\t", cats)
    
    cats.append('Smokey')
    print("Added Smokey to the end of the list with 'cats.append()'\n\t", cats)
    
    cats.remove('Smokey')
    print("Removed the first Smokey from list with 'cats.remove()'\n\t", cats)
    
    print("\nUsing index -1 prints the last element of the list \nIn this example it is: ", cats[-1], "\n")

    cats.insert(2,'Charly')
    print("\nInserting Charly to the list after the 2nd element:\n\t", cats)
    
    # Printing the list sorted changing the list
    print("\nSorting my cat's list without permanently changing their positions:\n\t", sorted(cats))
    print("\nMy cat's list is still the same:\n\t", cats)
 
    # Let's now sort the list
    cats.sort()
    print("\nSorting my cat's list:\n\t", cats)
    cats.sort(reverse=True)
    print("\nSorting my cat's list in reverse order:\n\t", cats)
    
def working_with_lists():
    family_members = ['sophie', 'bruno', 'jeannette', 'jean charles']
    
    print("\nLooping thru the list ...")
    for member in family_members:
        print("\n\t" + member.title() + " is part of my family")
        
    print("\nMaking Numerical Lists ...")
    #Using range() to make a list of numbers
    numbers = list(range(1,6))      #range(1,6) generates 1,2,3,4,5 and list() makes the list of numbers generated
    print("\n\t", numbers)
    even_numbers = list(range(0,11,2))
    print("\n\tEven numbers list: ", even_numbers)
    square_numbers = []     #Creates an empty list
    for i in range(0,11):
        square_numbers.append(i**2) #i**2 = i^2
    print("\n\tSquare numbers list: ", square_numbers) 
    #Another way to build te square list using a list comprehension
    squares = [value**2 for value in range (0,11)]
    print("\t\t\t\t", squares)
    
    print("\nCopying lists ...")
    my_foods = ['french fries', 'spaghetti']
    friend_foods = my_foods[:]                  #This creates a new list friend_foods by copy
    print("My preferred food's list:\t", my_foods)
    print("My friend food's list:\t\t", friend_foods)
    my_foods.append('olives')
    friend_foods.append('cake')
    print("Adding a food to my list:\t\t", my_foods )
    print("Adding a food to my friend list:\t", friend_foods)
    print("We can see that both lists are separate")
    
    friend_foods = my_foods     # This does not create a new list, it assigns the same list to both variables
                                # In other words we just created another pointer pointing the same list
                                #The following code shows it ...
    print("\nMy preferred food's list:\t", my_foods)
    print("My friend food's list:\t\t", friend_foods)
    my_foods.append('chorizo')
    friend_foods.append('peanuts')
    print("Adding a food to my list:\t\t", my_foods )
    print("Adding a food to my friend list:\t", friend_foods)
    print("We can see that both lists are the same")
                                
# Dictionaries
# 
# Let's see how to access the information once it’s in a dictionary and how to modify that information.
# Because dictionaries can store an almost limit less amount of information, I’ll show you how to loop
# through the data in a dictionary. Additionally, you’ll learn to nest dictionaries inside lists, 
# lists inside dictionaries, and even dictionaries inside other dictionaries.
# Understanding dictionaries allows you to model a variety of real­world objects more accurately. 
# You’ll be able to create a dictionary representing a person and then store as much information as you want
# about that person. You can store their name, age, location, profession, and any other
# aspect of a person you can describe. You’ll be able to store any two kinds of information that can be matched up
# such as a list of words and their meanings, a list of people’s names and their favorite numbers,
# a list of mountains and their elevations, and so forth   
def dictionaries_basics():
    print("\n\nWorking with dictionaries in Python ....")
    # A dictionary is a collection of key-value pairs. Each key is connected to a value, 
    # and you can use a key to access the value associated with that key.
    # A key’s value can be a number, a string, a list, or even another dictionary.
    # In fact, you can use any object that you can create in Python as a value in a dictionary.
    # In Python, a dictionary is wrapped in braces, {}, with a series of keyvalue pairs inside the braces.
    alien_0 = {'color': 'green'}                    # A dictionary to define a 'green' alien
    
    print("\n. Example of Alien dictionary alien_0:\t", alien_0)
    print(". Accessing value associated with a key alien_0['color']:\t", alien_0['color'])
    
    #Adding key/value pairs to the dictionary alien_0
    alien_0['points'] = 5
    alien_0['x_coord'] = 0
    alien_0['y_coord'] = 25
    print(". Adding keys to alien_0:\t", alien_0)
    
    #We can also start with an empty dictionary and add values to it
    alien_0 = {}
    alien_0['color'] = 'green'
    alien_0['points'] = 5
    print(". Started w/empty dict and populated real time alien_0:\t", alien_0)
    
    #Modifying a value
    print(". Modify value alien_0['color'] = 'blue")
    alien_0['color'] = 'blue'
    print("\talien_0 is now blue:\t", alien_0)
    
    #Removing information from alien_0 dict
    print(".Removing the key 'points' from alien_0 'del alien_0['points']'")
    del alien_0['points']
    print("\talien_0:\t", alien_0)
    
    # Using get() to Access Values
    # Using keys in square brackets to retrieve the value you’re interested infrom a dictionary might 
    # cause one potential problem: if the key you ask for doesn’t exist, you’ll get an error.
    # The get() method requires a key as a first argument. As a second optional argument, you can pass
    # the value to be returned if the key doesn’t exist:
    print(".Accessing values with get() method alien_0.get('color'):\t",alien_0.get('color'))
    print(".Using get() method to access alien_0 value that doesn't exist")
    print("\talien_0.get('position', 'No position assigned'):\t",alien_0.get('position', 'No position assigned'))
    

    
def working_with_dictionaries():
    
    #Looping thru a dictionary
    print("\n------ Looping Through a Distionary -------\n")
    user_0 = {
        'username' : 'jcpina',
        'first' : 'jean charles',
        'last' : 'pina',
        }
    
    print("Looping through all key-value pairs")
    for key, value in user_0.items():
        print("\nkey:\t", key)
        print("value:\t", value)
        
    print("\nLooping through all keys")
    for value in user_0.keys():
        print("\nkey:\t", value)
        
    print("\nLooping through all values")
    for value in user_0.values():
        print("\nvalue:\t", value)

    print("\nLooping through all keys in a particular order")
    for value in sorted(user_0.keys()):
        print("\nkey:\t", value)
        
    #The set method ...
    # The above approach pulls all the values from the dictionary without checking for repeats.
    # That might work fine with a small number of values, but in a poll with a large number of data,
    # You might have duplicated values and would result in a very repetitive list.
    # To see only the unique values without repetition, we can use a set ...
    # A set is a collection in which each item must be unique:    
    #     The keys() method is useful when you don’t need to work with all of the
    favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
        }
    # We can loop thru the favorite_languages dictionary values and only list one time 'python'
    print("\nUsing set() to remove repetitions in the data")
    print("In 'favorite_languages' dictionary python repeats:\t", favorite_languages)
    
    print("Using set() to avoid repetitions\n\tLanguages listed in 'favorite_languages':")
    for language in set(favorite_languages.values()):
        print("\t\t", language.title())
        
    # Sometimes we want to store multiple dictionaries in a list, or a list of items as a value in a dictionary.
    # This is called nesting. You can nest dictionaries inside a list, a list of items inside a dictionary, 
    # or even a dictionary inside another dictionary. Nesting is a powerful feature.
    # The Eric Matthes, Python_crash... book has good examples of the feature

    
''' Now lets use lists with something useful ...
    with the MENU FUNCTION ...
    The function prints a list of possible answers and a question,
    It returns the answer chosen by the user.
    
    Added a simple error handling with the try and except key words
'''
def menu(mylist, question):
    while (1):
        for entry in mylist:
            print (mylist.index(entry) + 1, ")", entry.title()) #+1 accommodates index starting @ 0
        try:
            return(int(input(question)) - 1)            #-1 accommodates index starting @ 0
        except:
            print("Enter a correct number ...")
            
# list_basics()
# working_with_lists()

# members = ['bruno', 'sophie', 'jeannette', 'tom', 'anis', 'lia', 'florence']
# male_members = ['bruno', 'tom', 'anis']
# joke = ('\t ... et vous avez besoin de lunettes !!!', '\t ... et vous avez tres bon gout !!!')
# joke_index = 1
# res = menu(members, 'qui est plus joli(e) ?\t')
# print("\n\tVous avez choisi:\t", members[res].title())
# for value in male_members:
#     if members[res] == value:
#         joke_index = 0
#         break
#
# print(joke[joke_index])

#Dictionary basic functions demo
dictionaries_basics()
working_with_dictionaries()

        



