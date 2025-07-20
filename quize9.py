#n = int(input("Enter the number of colors to guess (5): "))
n = int(input())

#n = int(input("Enter a number: "))
x = int(input())

for i in range(1, n + 1):
    if x % 2 == 0:
        x = x / 2
    else:
        x = x * 2 - 1
print(f"{x:.0f}")
