# continue:
# ---------

# Skips the current iteration and moves to thr next one.

for i in range(10):
    if i == 5:
        continue    # Spik the itreation when the value of i will become 5
    print(i, end=" ")

# output: 0 1 2 3 4 6 7 8 9  5 is skipped
    