#Program make a simple calculator that can add, subtract, multiply and divide using functions

#Import
import time

#Welcoming
print("Welcome to calculator.py by\nVishuMallela!")
time.sleep(2)
print("View my profile\n@ https://github.com/VishuMallela")
time.sleep(2)
print("\nHope you enjoy this project!")
time.sleep(2)
print("\nDon't forget to check out my other projects.")
time.sleep(2)
print("\nThis project is also featured in www.thecomputerprogrammers.wordpress.com!")
time.sleep(2)
print("\nWe prefer you running this project in fullscreen as it takes a lot of space.")
time.sleep(3)

# define functions
def add(x, y):
   """This function adds two numbers"""

   return x + y

def subtract(x, y):
   """This function subtracts two numbers"""

   return x - y

def multiply(x, y):
   """This function multiplies two numbers"""

   return x * y

def divide(x, y):
   """This function divides two numbers"""

   return x / y

# take input from the user
print("\nSelect the desired operation:")
time.sleep(0.5)
print("\n1.Add")
time.sleep(0.5)
print("2.Subtract")
time.sleep(0.5)
print("3.Multiply")
time.sleep(0.5)
print("4.Divide")
time.sleep(2)

choice = input("\nEnter choice(1/2/3/4):")
time.sleep(1)

num1 = int(input("\nEnter first number: "))
time.sleep(1)
num2 = int(input("\nEnter second number: "))
time.sleep(1)

if choice == '1':
   time.sleep(1)
   print("\n")
   print(num1,"+",num2,"=", add(num1,num2))
   time.sleep(1)
   print("\nThank you for using this program!")
   time.sleep(1)
   print("\nLoop function to be added soon!")
   time.sleep(1)
   print("\nRestart this program in the shell to view it again!")
   time.sleep(1)
   print("\nDon't forget to check out my other projects @ github.com/VishuMallela!")
   time.sleep(2)
   print("\nGoodbye and thank you for using this program!")
   time.sleep(2)
   print("\n:D")
   time.sleep(3)

elif choice == '2':
   time.sleep(1)
   print("\n")
   print(num1,"-",num2,"=", subtract(num1,num2))
   time.sleep(1)
   print("\nThank you for using this program!")
   time.sleep(1)
   print("\nLoop function to be added soon!")
   time.sleep(1)
   print("\nRestart this program in the shell to view it again!")
   time.sleep(1)
   print("\nDon't forget to check out my other projects @ github.com/VishuMallela!")
   time.sleep(2)
   print("\nGoodbye and thank you for using this program!")
   time.sleep(2)
   print("\n:D")
   time.sleep(3)

elif choice == '3':
   time.sleep(1)
   print("\n")
   print(num1,"*",num2,"=", multiply(num1,num2))
   time.sleep(1)
   print("\nThank you for using this program!")
   time.sleep(1)
   print("\nLoop function to be added soon!")
   time.sleep(1)
   print("\nRestart this program in the shell to view it again!")
   time.sleep(1)
   print("\nDon't forget to check out my other projects @ github.com/VishuMallela!")
   time.sleep(2)
   print("\nGoodbye and thank you for using this program!")
   time.sleep(2)
   print("\n:D")
   time.sleep(3)
   
elif choice == '4':
   time.sleep(1)
   print("\n")
   print(num1, "/", num2, "=", divide(num1,num2))
   time.sleep(1)
   print("\nThank you for using this program!")
   time.sleep(1)
   print("\nLoop function to be added soon!")
   time.sleep(1)
   print("\nRestart this program in the shell to view it again!")
   time.sleep(1)
   print("\nDon't forget to check out my other projects @ github.com/VishuMallela!")
   time.sleep(2)
   print("\nGoodbye and thank you for using this program!")
   time.sleep(2)
   print("\n:D")
   time.sleep(3)

else:
   time.sleep(1)
   print("\nInvalid Input, Restart Program")
   time.sleep(3)