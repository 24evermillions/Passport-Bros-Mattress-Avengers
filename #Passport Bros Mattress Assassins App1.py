#Passport Bros Mattress Assassins App

print('Thank You for downloading The Passport Matress Assassins App!')
print('Please follow directions and answer all questions to gain access to this amazing travel tool!')

name = input("Please enter Your name to begin:")#consult IP's input function journal notes if you need a refresher


############################################While Loops##################################################################
#consult IP's While loop journal notes if you need to refresh on while loops
while name == "":#if the user enters nothing this code here will loop until the usser enters a name
    print("User did not enter his name")
    name = input("Enter your name to begin the game: ")
print(f"Welcome {name} Your Journey Around the World Starts Now!")

age = int(input("Enter Your age to begin the game: "))#consult IP's input functions journal notes if you need a refresher 
##########################################################################################################################


while age < 0 or age < 18:#consult IP's or opereator journal notes if you need a refresher
    print("You must be 18 and above to access app, and Age cant be negative !")
    age = int(input("Enter Your age to begin game: "))#consult IP's input function journal notes if you need a refresher

print(f"Thanks for confirming that you are a {age} years old and of age to use the app")

############################################################################################################################

##Papi Chulos Code##
#name=input('Please Enter Your Name To Begin')

#while name=="":

#    name=input('Enter Your Name Please:')
#    print(f'Welcome {name} Your Journey Around the \World Starts Now!') 

#name=int(input('You must be atleast 18 to use the app', 'Enter your age'))
#while age>=18:
#    print(f'Thanks for confirming you are {age} years old and of age to use the app!')
    
