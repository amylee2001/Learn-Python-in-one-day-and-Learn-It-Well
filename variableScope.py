message1 = "Global Variable (shares same name as a local variable)"

def myFunction():
    message1 = "Local Variable (shares same name as a global variable)"
    print("\nINSIDE THE FUNCTION")
    print (message1)

#Calling the function
myFunction()

#Printing message1 OUTSIDE the function
print ("\nOUTSIDE THE FUNCTION")
print(message1)


message1 = "Global Variable"

def myFunction():
    print("\nINSIDE THE FUNCTION")
#Global variables are accessible inside a function
    print (message1)
    #Declaring a local variable
    message2 = "Local Variable"
    print (message2)

'''
Calling the function
Note that myFunction() has no parametrers.
Hence, when we call this function,
we use a pair of empty parentheses.
'''
myFunction()

print("\nOUTSIDE THE FUNCTION")

#Global variables are accessible outside function
print(message1)
#Local variables are NOT accessible outside function.
print(message2)

message1 = "Global Variable (shares same name as a local variable)"

def myFunction():
    message1 = "Local Variable (shares same name as a global variable)"
    print("\nINSIDE THE FUNCTION")
    print (message1)

#Calling the function
myFunction()

#Printing message1 OUTSIDE the function
print ("\nOUTSIDE THE FUNCTION")
print(message1)
