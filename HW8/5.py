'''
Implement the function count( lst, item) . Returns the number of times item appears in lst.
For Example:
If lst is [0, 32, ‘a’, ‘0’, ‘4’, 15, ‘q’, ‘0’] and item is ‘0’, it returns 2
'''

def count(lst, item):
    return lst.count(item)

print(count([0, 32, 'a', '0', '4', 15, 'q', '0'], 0))