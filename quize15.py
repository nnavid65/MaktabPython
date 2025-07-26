def get_user_input():
    #return int(input("Please enter a number: "))
    a = int(input())
    b = int(input())
    return a, b

def square_number(a, b=0):
    a = a * a
    b = b * b
    return a, b

def sum_of_squares(a, b=0):
    return a + b

get_user_number = get_user_input()
calculated_square = square_number(get_user_number[0], get_user_number[1])
sum_two_squares = sum_of_squares(calculated_square[0], calculated_square[1])
#print(calculated_square)
print(sum_two_squares)