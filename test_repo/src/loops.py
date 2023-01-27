'''
A Simple program illustrating loops in python
Created on Nov 16, 2022

@author: jcp
'''

def looping():
    
    #The while loop
    a = 0
    while a < 10:
        a = a + 1
        print(a)
    
    print("End of while")
    
    # Adding if statements..
    # Equality(==), Inequality(!=), less than(<), less or equal (<=)
    # Multi conditions (and, or)
    # Value in a list ... list_item in my_list and not in list ... list_item not in my_list 
    # The if-elif-else chain
    # if a > b
    #    .. do something
    # elif a > c
    #    .. do something
    # else
    #    .. do something
    
    print("\nThese are the even numbers between 0 and 20")
    value = 0
    while value <= 20:
        if value % 2 == 0:
            print(value)
        value = value + 1
    
    print("End of if")
    print("You can also use, if, elif and else")
    
    #The for loop
    print("\nGenerating Square Numbers")
    for value in range(1,11):
        print("Square of ", value, " is : ", value**2)
    print("End of for loop")
    
#----------------------- Some exercises -----------------------------------------   
# Checking Usernames: Do the following to create a program that simulates
# how websites ensure that everyone has a unique username.
# •     Make a list of five or more usernames called current_users.
# •     Make another list of five usernames called new_users. Make sure one or
#       two of the new usernames are also in the current_users list.
# •     Loop through the new_users list to see if each new username has already
#       been used. If it has, print a message that the person will need to enter a
#       new username. If a username has not been used, print a message of welcoming
# •     Make sure your comparison is case insensitive. If 'John' has been used,
#       'JOHN' should not be accepted. (To do this, you’ll need to make a copy of
#       current_users containing the lowercase versions of all existing users.)
def check_names(u_current, u_new):
    if u_new and u_current:       # Check the list is not empty
        for user in u_new:
            if user.lower() not in u_current:
                print("\tWelcome: ", user.title())
                if user.lower() == 'admin':
                    print("\tWould you like to see a status report?")
            else:
                print("\t!! user name", user.lower(), " not available!!!")
    else:
        print("We need to find some users")
        
#looping()

current_users = ['admin', 'jc', 'jeanne', 'marcel', 'charly']
new_users = ['bruno', 'lia', 'admin', 'pascal', 'paul', 'jc', 'jack']
check_names(current_users, new_users)

 
    