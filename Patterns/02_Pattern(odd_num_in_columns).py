#steps to solve the pattern
# 1. for the outer loop, count the number of line or rows
# 2. for the inner loop, focus on the colums and connect them somehow to the rows
# 3. print them "*" inside the inner for loop
# 4. observe symmettry [optional]


num = int(input("enter the row: "))
k = 1
for i in range(1, num+1):
    for j in range(1, k+1):
        print("x", end=" ")
    k = k + 2
    print()
 