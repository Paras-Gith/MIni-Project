#steps to solve the pattern
# 1. for the outer loop, count the number of line or rows
# 2. for the inner loop, focus on the colums and connect them somehow to the rows
# 3. print them "*" inside the inner for loop
# 4. observe symmettry [optional]


rows = int(input("enter the number of rows: "))
for i in range(1, rows+1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()

