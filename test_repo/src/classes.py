'''
Illustrating basic classes functionality

Created on Nov 20, 2022

@author: jcp
'''

print("Module name:\t", __name__, '\n')    

# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
if __name__ == '__main__':
    print("\n\t\t------- Exercise 9.1 ----------\n")

class Restaurant:
    def __init__(self, name, food_type):
        self.restaurant_name = name
        self.cuisine_type = food_type
        self.numbered_served = 0            #Addition from exercise 9.4
        
    def describe_restaurant(self):
        print("Restaurant", self.restaurant_name.title(), "is specialized in", self.cuisine_type, "food")
        
    def open_restaurant(self):
        print(self.restaurant_name.title(), "is now open !!!")
        
    def set_number_served(self, n_served):
        self.numbered_served  = n_served
        
    def increment_number_served(self, delta):
        self.numbered_served += delta
        
if __name__ == '__main__':

    # Make an instance called restaurant from your class.
    # Print the two attributes individually, and then call both methods.
    restaurant_la_madeleine = Restaurant('la madeleine', 'french')
    
    print("Restaurant Name:\t", restaurant_la_madeleine.restaurant_name.title())
    print("Restaurant Food Type:\t", restaurant_la_madeleine.cuisine_type.upper())
        
    restaurant_la_madeleine.describe_restaurant()
    restaurant_la_madeleine.open_restaurant()
    
    # 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
    # different instances from the class, and call describe_restaurant() for each
    # instance.
    print("\n\t\t------- Exercise 9.2 ----------\n")
    restaurant_1 = Restaurant('McDonalds', 'fastfood')
    restaurant_2 = Restaurant('signorizza', 'italian')
    restaurant_3 = Restaurant('le port', 'seafood')
    
    restaurant_1.describe_restaurant()
    restaurant_2.describe_restaurant()
    restaurant_3.describe_restaurant()
    
    # 9-4. Number Served: Start with your program from Exercise 9-1 (page 162).
    # Add an attribute called number_served with a default value of 0. Create an
    # instance called restaurant from this class. Print the number of customers the
    # restaurant has served, and then change this value and print it again.
    print("\n\t\t------- Exercise 9.4 ----------\n")
    restaurant_4 = Restaurant('lo jun\'s', 'chinese')
    print("numbered of clients served at", restaurant_4.restaurant_name,":\t", restaurant_4.numbered_served)
    
    restaurant_4.numbered_served = 121
    print("numbered of clients served at", restaurant_4.restaurant_name,":\t", restaurant_4.numbered_served)
    
    print('\n')
    
    # Add a method called set_number_served() that lets you set the number
    # of customers that have been served. Call this method with a new number and print the value again.
    # Add a method called increment_number_served() that lets you increment the number of customers who’ve been served.
    # Call this method with any number you like that could represent how many customers were served in, say, a
    # day of business.
    restaurant_4.set_number_served(25)
    print("numbered of clients served at", restaurant_4.restaurant_name,":\t", restaurant_4.numbered_served)
    
    restaurant_4.increment_number_served(100)
    print("Total clients served in 1-day at", restaurant_4.restaurant_name,":\t", restaurant_4.numbered_served)
    
    
    # 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant.
    # . Write a class called IceCreamStand that inherits from the Restaurant class you wrote
    # in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of
    # the class will work; just pick the one you like better. 
    # . Add an attribute called flavors that stores a list of ice cream flavors.
    # . Write a method that displays these flavors.
    # . Create an instance of IceCreamStand, and call this method.
    print("\n\t\t------- Exercise 9.6 ----------\n")

class IceCreamStand(Restaurant):
    def __init__(self, name, food_type, flavors = None):
        # Initializes attributes for the parent class
        super().__init__(name, food_type)
        self.flavors = flavors
        
    def show_flavors(self):
        if self.flavors:
            print("Ice cream flavors:\t", self.flavors)
        else:
            print("You need to add some flavors")
        
if __name__ == '__main__':
        
    icecream_flavors = ['vanilla', 'chocolate', 'strawberry']         
    my_ice_cream = IceCreamStand('joe\'s icecream', 'icecream', icecream_flavors)
    my_ice_cream.show_flavors()
    
    # 9-7. Admin: An administrator is a special kind of user.
    # . Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 
    # . Add an attribute, privileges, that stores a list of strings like "can add post",
    # "can delete post", "can ban user", and so on.
    # . Write a method called show_privileges() that lists the administrator’s set of privileges.
    # . Create an instance of Admin, and call your method.
    print("\n\t\t------- Exercise 9.7 ----------\n")

class User:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname
    
    def describe_user(self):
        print("User First Name:\t", self.first_name.title(), "\nUser Last  Name:\t", self.last_name.title())
    
    def greet_user(self):
        print("Good morning", self.first_name.title(), self.last_name.title() )

if __name__ == '__main__':
    user_1 = User('jean charles', 'pina')
    user_1.describe_user()
    user_1.greet_user()
    
    print("\n")

class Admin(User):
    def __init__(self, fname, lname, p = None):
        # Initializes attributes for the parent class
        super().__init__(fname, lname)
        self.privileges = p
        
    def show_privileges(self):
        print("Here is the list of admin privileges\n\t\t", self.privileges)

if __name__ == '__main__':
    admin_privileges = ['can add post', 'can delete post', 'can ban user']        
    admin = Admin('joe', 'smith', admin_privileges)
    admin.show_privileges()
            
     
    # 9-8. Privileges:
    # . Write a separate Privileges class. The class should have one attribute, privileges,
    # that stores a list of strings as described in Exercise 9-7.
    # . Move the show_privileges() method to this class.
    # . Make a Privileges instance as an attribute in the Admin class.
    # . Create a new instance of Newadmin and use your method to show its privileges.
    print("\n\t\t------- Exercise 9.8 ----------\n")

class Privileges():
    def __init__(self, plist):
        self.privileges = plist
        
    def show_privileges(self):
        print("Here is the list of your privileges\n\t\t", self.privileges)

class Newadmin(User):
    def __init__(self, fname, lname, lp):
        # Initializes attributes for the parent class
        super().__init__(fname, lname)
        # Add a class attribute Privileges
        self.privileges = Privileges(lp)
        
    def greet_admin(self):
        self.greet_user()
        print("\tYou are an administrator ...")
        self.privileges.show_privileges()
        
if __name__ == '__main__':
    new_admin = Newadmin('jeanne', 'pina', admin_privileges)
    new_admin.greet_admin()
    #new_admin.privileges.show_privileges() 

