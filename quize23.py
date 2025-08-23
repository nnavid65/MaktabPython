# error handeling 

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except Exception as e:
        return "Error: " + str(e)
    else:
        return result
    finally:
        print("Execution completed.")
    
def get_integer_input(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        #except Exception as e:
        #    print("Error:", e)
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    num1 = get_integer_input("Enter the first integer: ")
    num2 = get_integer_input("Enter the second integer: ")
    print("Division Result:", divide(num1, num2))

if __name__ == "__main__":
    main()