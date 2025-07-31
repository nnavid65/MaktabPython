def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

def get_numbers():
    numbers = (input())
    return [int(num) for num in numbers.split()]

num_list = get_numbers()
result = sum_numbers(*num_list)
print(result)