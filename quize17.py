def is_greater(a, b):
    if a > b:
        return True
    else:
        return False
    
def get_numbers():
    #return int(input("Enter two numbers separated by space: "))
    a = int(input())
    b = int(input())
    return a, b

num1, num2 = get_numbers()
check_num = is_greater(num1, num2)
print(check_num)