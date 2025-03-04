CODE : 
import math
import numpy as np

def basic_operations():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = input("Enter choice (1/2/3/4): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == '1':
        print(f"Result: {num1 + num2}")
    elif choice == '2':
        print(f"Result: {num1 - num2}")
    elif choice == '3':
        print(f"Result: {num1 * num2}")
    elif choice == '4':
        if num2 != 0:
            print(f"Result: {num1 / num2}")
        else:
            print("Error: Division by zero!")
    else:
        print("Invalid input")

def trigonometric_operations():
    print("Select function:")
    print("1. Sine")
    print("2. Cosine")
    print("3. Tangent")
    choice = input("Enter choice (1/2/3): ")
    angle = float(input("Enter angle in degrees: "))
    radian = math.radians(angle)
    
    if choice == '1':
        print(f"sin({angle}) = {math.sin(radian)}")
    elif choice == '2':
        print(f"cos({angle}) = {math.cos(radian)}")
    elif choice == '3':
        print(f"tan({angle}) = {math.tan(radian)}")
    else:
        print("Invalid input")

def logarithmic_operations():
    num = float(input("Enter a number: "))
    if num > 0:
        print(f"log({num}) = {math.log(num)}")
    else:
        print("Error: Logarithm undefined for non-positive numbers")

def matrix_operations():
    print("Matrix Operations:")
    print("1. Addition")
    print("2. Multiplication")
    choice = input("Enter choice (1/2): ")
    
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    
    print("Enter elements of first matrix:")
    matrix1 = np.array([[float(input()) for _ in range(cols)] for _ in range(rows)])
    print("Enter elements of second matrix:")
    matrix2 = np.array([[float(input()) for _ in range(cols)] for _ in range(rows)])
    
    if choice == '1':
        print("Matrix Addition Result:")
        print(matrix1 + matrix2)
    elif choice == '2':
        print("Matrix Multiplication Result:")
        print(np.dot(matrix1, matrix2))
    else:
        print("Invalid input")

def main():
    while True:
        print("\nAdvanced Calculator")
        print("1. Basic Arithmetic")
        print("2. Trigonometric Functions")
        print("3. Logarithm")
        print("4. Matrix Operations")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            basic_operations()
        elif choice == '2':
            trigonometric_operations()
        elif choice == '3':
            logarithmic_operations()
        elif choice == '4':
            matrix_operations()
        elif choice == '5':
            print("Exiting calculator...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
