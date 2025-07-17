z = 1 + 2j; 
# 1 --> real number
# 2j --> imaginay number

print(f"real part: {z.real}")
print(f"imaginary nunber: {z.imag}")

z1 = 2 + 3j
z2 = 1 - 2j
sum_z = z1 + z2
print(f"Sum of ({z1}) and ({z2}): {sum_z}")
diff_z = z1 - z2
print(f"difference of ({z1}) and ({z2}): {diff_z}")
prod_z = z1 * z2
print(f"Product of ({z1}) and ({z2}): {prod_z}")
quot_z = z1 / z2
print(f"Quotient of ({z1}) and ({z2}): {quot_z}")
mag_z1 = abs(z1)
print(f"Absolute of ({z1}): {mag_z1}")


# One method to create complex number
z3 = complex(2, 3)
print(z3)