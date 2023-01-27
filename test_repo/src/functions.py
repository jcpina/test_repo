'''
Simple program showing an example of a basic function

Created on Nov 20, 2022

@author: jcp
'''

def calculator():
    print("Now let's use a function which actually does something ...")
    choice = -1
    res = 0
    while choice != 0:
        choice = int(input("What is your choice 1 (A), 2 (S), 3 (M), 4 (D), 0 (Q): "))
        if (choice > 0 and choice < 5):
            op1 = int(input("Enter operand 1: "))
            op2 = int(input("Enter operand 2: "))
            print(type(op1))
            print(type(op2))
            if choice == 1:
                res = op1 + op2
            elif choice == 2:
                res = op1 - op2
            elif choice == 3:
                res = op1 * op2
            elif choice == 4:
                res = op1 / op2
            print("Result of operation: ", res)
        elif choice != 0:
                print("Undefined operand: ", choice)
    
    print("End of calculator()")

# Problem:    
# Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt. The function should print
# a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the
# function a second time using keyword arguments.
def make_shirt(size, message):
    print("Your shirt size is:\t", size)
    print("Your message is:\t", message)
    
#call to make_shirt using positional arguments
make_shirt('M', 'Lone Star State')

#call to make_shirt using keyword arguments
make_shirt(message='Large Boy', size='XXL')
print("\n")

# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message.
def make_shirt_bis(message='I Love Python', size='L'):
    print("Your shirt size is:\t", size)
    print("Your message is:\t", message)

#call to make_a large shirt with 'I Love Python'
make_shirt_bis()

#call to make_a medium shirt with 'I Love Python'
make_shirt_bis(size='M')

#call to make_a medium shirt with 'I Love Python'
make_shirt_bis(message='I wish Portugal wins!!!', size='S')
print("\n")


# 8-5. Cities: Write a function called describe_city() that accepts the name of
# a city and its country. The function should print a simple sentence, such as
# Reykjavik is in Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the default country
def city_description(city, country='Portugal'):
    print(city, "is in", country)

city_description('Lisbon')
city_description('Madrid', 'Spain')
city_description('Obidos')

print("\n")

# 8-6. City Names: Write a function called city_country() that takes in the name
# of a city and its country. The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the values that are returned.
def city_country(city, country):
    ret = city + ', ' + country
    return ret

print(city_country('Lisbon', 'Portugal'))
print(city_country('Paris', 'France'))
print(city_country('Austin', 'USA'))

# 8-7. Album: Write a function called make_album() that builds a dictionary describing a music album.
# The function should take in an artist name and an album title, and it should return a dictionary
# containing these two pieces of information.
# Use the function to make three dictionaries representing different albums. 
# Print each return value to show that the dictionaries are storing the album information correctly.
# Use None to add an optional parameter to make_album() that allows you to # store the number of songs on an album.
# If the calling line includes a value for the number of songs, add that value to the album’s dictionary. Make at least
# one new function call that includes the number of songs on an album.
def make_album(artist_name, album_title, Ntracks=None):
    music_album = {'artist_name':artist_name, 'album_title': album_title}
    if Ntracks:
        music_album['Ntracks'] = Ntracks
        
    return music_album

album_1 = make_album('Barbara Pravi', 'Les prieres - racines')
album_2 = make_album('Bean Mazue', 'Paradis', 14)
album_3 = make_album('Daniel Balavoine', 'Sauver l amour', 9)

print(album_1)
print(album_2)
print(album_3)

print('\n')

# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop

while(1):
    new_album = input("\nDo you want to enter new album [yes/no]? ")
    if new_album.lower() == 'no':
        break;
    else:
        artist_name = input("Enter artist name: ")
        album_name = input("Enter album name: ")
        
        album = make_album(artist_name, album_name)
        print(album)
        
print("End of loop")
print()

# 8-9. Messages: Make a list containing a series of short text messages. Pass the
# list to a function called show_messages(), which prints each text message.
def show_messages(message_list):
    while message_list:
        message = message_list.pop();
        print(message)
        
messages_to_show = ["Make a list", "Series of short messages", "Pass the list"]
show_messages(messages_to_show)
print('\n')

# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
# Write a function called send_messages() that prints each text message and
# moves each message to a new list called sent_messages as it’s printed. After
# calling the function, print both of your lists to make sure the messages were moved correctly.
def send_messages(message_to_send, messages_sent):
    while message_to_send:
        message = message_to_send.pop();
        print("Sending the message ...", message)
        messages_sent.append(message)
        
messages_to_show = ["Make a list", "Series of short messages", "Pass the list"]
messages_sent = []
send_messages(messages_to_show, messages_sent)
print("Messages to send:\t", messages_to_show)
print("Messages sent:\t", messages_sent)
print('\n')

# 8-11. Archived Messages: Start with your work from Exercise 8-10. Call the
# function send_messages() with a copy of the list of messages. After calling the
# function, print both of your lists to show that the original list has retained its
# messages.
messages_to_show = ["Make a list", "Series of short messages", "Pass the list"]
messages_sent = []
send_messages(messages_to_show[:], messages_sent)
print("Messages to send:\t", messages_to_show)
print("Messages sent:\t", messages_sent)
print("\n")
    