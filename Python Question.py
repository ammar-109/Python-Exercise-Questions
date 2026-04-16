1-Reversed string

def string_operations(text):
    reversed_str = text[::-1]
    every_second = text[::2]
    return reversed_str, every_second
------------------------------------------
2-List of comparison of even numbers 

numbers = [1, 2, 3, 4, 5, 6]
squares_of_evens = [x**2 for x in numbers if x % 2 == 0]

print(squares_of_evens) 
----------------------------------------------------------
3-Chracter Frequency Distribution
def char_frequency(text):
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return freq

print(char_frequency("banana")) 
-----------------------------------------------------------
4-Indices of odd number
def odd_indices(lst):
    return [i for i, val in enumerate(lst) if val % 2 != 0]

print(odd_indices([10, 21, 32, 43, 54])) 
-----------------------------------------------------------
5-Rotate list right by k positions
def rotate_right(lst, k):
    if not lst:
        return lst
  
    k = k % len(lst)
    return lst[-k:] + lst[:-k]
print(rotate_right([1, 2, 3, 4, 5], 2))  
----------------------------------------------------------
6-Dictionary from Two Lists
def lists_to_dict(keys, values):
    return dict(zip(keys, values))

print(lists_to_dict(['a', 'b'], [1, 2])) 
----------------------------------------------------------
7-Manuak iteration by exception handling
def manual_iterate(lst):
    it = iter(lst)
    while True:
        try:
            element = next(it)
            print(element)
        except StopIteration:
            print("Iteration complete.")
            break
manual_iterate([10, 20, 30])
----------------------------------------------------------
8-Flatten a nested List
def flatten(nested_lst):
    return [item for sublist in nested_lst for item in sublist]

print(flatten([[1, 2], [3, 4], [5]])) 
----------------------------------------------------------
9-Palindrome Check
def is_palindrome(text):
    return text == text[::-1]

print(is_palindrome("racecar")) 
----------------------------------------------------------
10-Second Largest number (NoSorting)
def second_largest(numbers):
    if len(numbers) < 2:
        return None
    first = second = float('-inf')
    for n in numbers:
        if n > first:
            second = first
            first = n
        elif n > second and n != first:
            second = n
    return second if second != float('-inf') else Non
print(second_largest([10, 20, 4, 45, 99])) 
---------------------------------------------------------
