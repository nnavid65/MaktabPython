def is_positive(n):
    return n >= 0

def get_number():
    #return int(input("Enter a number: "))
    return int(input())

#n = int(input("Enter a number: "))
#num = int(input())
num = get_number()
check_num = is_positive(num)
print(check_num)