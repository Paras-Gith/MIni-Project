#steps to solve the pattern
# 1. for the outer loop, count the number of line or rows
# 2. for the inner loop, focus on the colums and connect them somehow to the rows
# 3. print them "*" inside the inner for loop
# 4. observe symmettry [optional]

def pattern(n):
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print()

def main():
    n = int(input("enter the number: "))
    pattern(n)
if __name__ == "__main__":
    main()