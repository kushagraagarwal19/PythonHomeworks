'''
Create a list of the first n powers of 2. Ask user for n.
For Example:
If n = 4, create a list [2, 4, 8, 16]
'''

def myList(n):
    l = []
    for i in range(1,n+1):
        l.append(pow(2,i))
    print(l)

n = int(input("Please enter n "))
myList(n)