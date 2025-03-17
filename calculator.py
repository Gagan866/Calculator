def add(a, b):
    return a + b

def main():
   
    print("Simple Addition Calculator")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = add(num1, num2)
    print(f"The result of {num1} + {num2} is {result}")

if __name__ == "__main__":
    main()

