fruits = ('apple', 'mango', 'banana', 'date')
for fruit in fruits:
    print(fruit, end=" ")
print()    


# iterating tuple using enumerate
colors = ("red", "Green", "blue")
for t in enumerate(colors):  # enumerate returns a tuple 
    print(t, end=" ")
print()

# unpacking tuple returned by the enumerate(colors)
for index, color in enumerate(colors, start=11):  # enumerate returns a tuple 
    print(index, color)
print()

 
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
for number, letter in pairs:
    print(number, letter)
print()

# concatination and repetition
tuple1 = (1, 2, 3)
tuple2 = (4, 5)
result = tuple1 + tuple2
print(result)
print()


tuple1 = ('a', )
result = tuple1 * 3
print(result)
print(f"result * 0: {result * 0}\n")

tuple1 = (1, 2)
tuple2 = ()
print(f"tuple1 + tuple2: {tuple1+tuple2}")
print(f"tuple1 * -1: {tuple1* -1}\n")


colors = ("red", "green", "blue")
print(f"green not in colors: {"green" not in colors}")


tuple_a = (1, 2, 3)
tuple_b = (1, 2, 3)
tuple_c = (1, 2, 4)
print(f"(tuple_a == tuple_b): {tuple_a == tuple_b}")
print(f"(tuple_a == tuple_c): {tuple_a == tuple_c}")
print(f"(tuple_a < tuple_c): {tuple_a < tuple_c}")


# Methods --> count, index
numbers = (1, 5, 8, 2, 1, 4, 2, 3, 2)
print(f"numbers.count(2): {numbers.count(2)}")
print(f"numbers.index(2): {numbers.index(2)}")  # returns first occurrenec index of 2

# No tuple comprehension exists unlike list comprehension and dict comprehension because they are mutuable DS but tuple is immutable Ds