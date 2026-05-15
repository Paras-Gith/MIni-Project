def pattern4(n):
    for i in range(1, n+1):
        for j in range(i):
            print(i, end="")
        print()

def main():
    n = 5
    pattern4(n)

if __name__=="__main__":
    main()