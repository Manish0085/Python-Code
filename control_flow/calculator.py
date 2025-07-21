try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
except ValueError:
    print("❌ Please enter valid integers.")
    exit()

print("\nSelect an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulo")

operation = input("Enter your choice (1-5): ")

if operation == "1":
    operation_name = "Addition"
    result = a + b
elif operation == "2":
    operation_name = "Subtraction"
    result = a - b
elif operation == "3":
    operation_name = "Multiplication"
    result = a * b
elif operation == "4":
    operation_name = "Division"
    if b != 0:
        result = a / b
    else:
        print("❌ Cannot divide by zero.")
        exit()
elif operation == "5":
    operation_name = "Modulo"
    if b != 0:
        result = a % b
    else:
        print("❌ Cannot perform modulo with divisor 0.")
        exit()
else:
    print("❌ Invalid operation selected.")
    exit()

print(f"✅ {operation_name} of {a} and {b} is {result}")


