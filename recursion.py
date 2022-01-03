
def factorial(x):
    
    #checks if the number is greater than 0 
    if x < 0:
        return 0
    
    #checks if the number is equal to 1
    elif x == 1:
        return 1
    #calculates the factorial of the number 
    else :
        return x * factorial (x - 1)


number = int (input("input the factorial number: "))

print("the factorial is ", factorial(number))
