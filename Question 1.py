def outer(a, b):
    def inner(x,y):
        return (x + y)
    total = inner(a,b)
    addition = total + 5
    return addition
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
final = outer(num1, num2)
print("The addition of 2 numbers is: ", final)



