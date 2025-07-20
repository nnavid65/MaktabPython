# Majic MAchine Quiz
#n = int(input("Enter the number of colors to guess (5): "))
n = int(input())

while n != 1:
    if n % 2 == 0:
        n = n / 2
    else:
        n = n * 3 + 1
    print(f"{n:.0f}")