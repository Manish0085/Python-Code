import math
import decimal

a = 0.3
b = 0.1 + 0.2
print(math.isclose(a, b))

a = decimal.Decimal('0.1')
b = decimal.Decimal('0.2')
print(f"Sum of {a} and {b}: {a + b}")


pi = 3.14159265359
print(f"Rounded value of {pi} upto to 2: {round(pi, 2)}")

