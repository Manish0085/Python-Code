# break:
# -------

# Immediately break or exit the loop, regardless of the loop condition.

for i in range(10):
    print(i)
    if i == 5:
        break
print("Outside the loop")    