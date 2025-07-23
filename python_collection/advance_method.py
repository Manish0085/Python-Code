nums = [1, 2, 3]
nums.reverse()
print(f"reverse: {nums}")
print(f"reverse: {list(reversed(nums))}")

words = ["banana", "apple", "cherry"]
words.sort()
print(f"sorted List: {words}")
words.sort(key=len, reverse=True)
# default behaviour:
# my_list.sort(key=None, reverse=False)
print(f"sorted list on the basis of length of words: {words}")
# sort() modifies the same list doesn't create a new list

words = ["banana", "apple", "cherry"] 
sorted_list = sorted(words, key=len, reverse=True) # sorted() always creates a new list
print(sorted_list)


# custom sorting
nums = [-10, 5, -3, 2, -1]
nums.sort()
print(nums)
nums.sort(key=abs)
print(f"sorted list (key=abs): {nums}")

names = ["Alice", "ALice", "Charlie"]
print(sorted(names, key=str.lower))


fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
print(f"\"apple\" count in the list {fruits}: {fruits.count('apple')}")
print(f"\"kiwi\" count in the list {fruits}: {fruits.count('kiwi')}")
print(f"\"apple\" index in the list {fruits} after index 1: {fruits.index('apple', 1)}")