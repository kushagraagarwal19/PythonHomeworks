'''
Write a function that takes an integer myInt and a positive integer n as two arguments and
return a list of n consecutive integers that begins with myint.

For example:
If myInt = 10 and n = 5, your function should return the list [10, 11, 12, 13, 14].
'''

def myList(myInt, n):
    solution = []
    a = myInt
    for i in range(n):
        solution.append(a)
        a += 1
    return solution

print(myList(10,5))