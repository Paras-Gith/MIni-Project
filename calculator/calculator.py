a = int(input("Enter the number 1: "))
b = int(input("Enter the number 2: "))

operator = input("which operation to perform:" )

if(operator == "add" or "+"):
    print("Addition:", a+b)
elif(operator == "sub" or "-"):
    print("Subtraction:", a - b)       
elif(operator == "div" or "/"):
    print("division:", a / b)       
elif(operator == "mult" or "*"):
    print("multiplication:", a * b) 
else:
    print("Invalid operator!")    

