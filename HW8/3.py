'''
Problem 3
Write a function that takes a string of 1s and 0s as argument. The function will prints out the number of consecutive 1s and 0s.
Example Output:
>>> encodeBinary('1111000110')
4 1's
3 0's
2 1's
1 0's
'''

def encodeBinary(binaryString):
    stringLength = len(binaryString)
    count = 1
    for i in range(stringLength-1):
        if binaryString[i+1] == binaryString[i]:
            count = count + 1
        else:
            print(str(count) + ' ' + binaryString[i-1] + "'s")
            count = 1
    print(str(count) + ' ' + binaryString[i-1] + "'s")

encodeBinary('1111000110')