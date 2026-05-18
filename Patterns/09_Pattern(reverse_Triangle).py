def pattern(n):
    for row in range(n, 0, -1):
        for col in range(n-row):
            print(" ", end="")
        for col in range(2*row-1): 
            print("*", end="")
        print()

def main():
    n = 5
    pattern(n)

if __name__=="__main__":
    main()

