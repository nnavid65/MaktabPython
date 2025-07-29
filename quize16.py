def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
def get_number():
    #return int(input("Enter a number: "))
    return int(input())

num = get_number()
check_num = is_even(num)
print(check_num)