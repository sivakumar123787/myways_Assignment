from time import * #this will import all time bulitin functions
class signup:
    def __init__(self,name,userid,password): #init is  constructor
        self.name=name

        self.userid=userid
        self.password=password
    def display(self):    #this display function display the below information when it is called
        print("your signup sucess ")

    def login(self):  #this function checks the userid and password and go the next page

        if(self.userid==a and self.password==b):
            print("your login sucess wait for a second to go home page")
        else:
            print("please enter valid username and password")
    def home(self):   #this function display the home page description
        if (self.userid == a and self.password == b):
            __x = "MyWays provides a one step solution for all the career related problems.\n The services offered follow the 3-I model of Introspection, Information and Interaction.\n From career counseling through psychometric analysis to providing internships to networking and getting industrial guidance,\n MyWays helps the students end-to-end."              #this step will hide the home page data when user enters wrong username and password.
            print(__x)


        else:
             print("enter the correct username and password to access the home page")
name=input("enter the name")
userid=input("enter the userid")
password=input("enter tge password")
obj=signup(name,userid,password)  #object declartion
obj.display()                     #display function calling
sleep(2)                         #code will be sleep for 2 seconds
a = input("enter the userid")
b = input("enter the password")
obj.login()                     #login function calling
sleep(1)
obj.home()                       #home function calling

