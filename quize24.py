# write a decorator

import time


def returned_time(func):
    def wrapper(sec):
        start_time = time.time()
        result = func(sec)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper

@returned_time
def list_of_nums(num):
    return [i for i in range(num)]

def get_n():
    num = int(input("Enter a number: "))
    return num

def main():
    num = get_n()
    print("List of numbers:", list_of_nums(num))
    #print(time.time())


if __name__ == "__main__":
    main()

