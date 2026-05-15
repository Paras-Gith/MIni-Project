def pattern(n):
    for i in range(1, n+1):
        for j in range(n-i+1):
            print("*", end="")
        print()
        
def main():
    n = int(input("enter the value: "))
    pattern(n)

if __name__=="__main__":
    main()