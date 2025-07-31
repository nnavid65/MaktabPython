def is_evens(*args):
    evens = []
    for num in args:
        if num % 2 == 0:
            evens.append(num)
    return evens

def get_numbers():
    numbers = input()
    return [int(num) for num in numbers.split()]

my_list = get_numbers()
result = is_evens(*my_list)
print(result)