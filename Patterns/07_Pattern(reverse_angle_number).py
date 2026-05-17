def pattern(n):
    for row in range(1, n+1):
        for col in range(n-row+1):
            print(col + 1, end="")
        print()

def main():
    n = 5
    pattern(n)

if __name__=="__main__":
    main()