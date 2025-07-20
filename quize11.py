#n = int(input("Enter a number: "))
n = int(input())

if n % 3 == 0 and n % 5 == 0:
    print("افسانه ای")
elif n % 3 == 0:
    print("جادویی")
elif n % 5 == 0:
    print("نفرین شده")
else:
    print("معمولی")
