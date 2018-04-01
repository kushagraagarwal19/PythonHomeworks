number = int(input("Enter the number: "))

startBlanks = " "
endBlanks = " "
string = " "

# for i in range(2*number):
#     startBlanks = startBlanks*(i)
#     endBlanks = endBlanks*(i)
#     for j in range (2*number-1):
#         startBlanks = startBlanks*(j)
#         endBlanks = endBlanks*(j)
#         string = startBlanks + string + "*" + endBlanks
#     print(string)

list = []

for i in range(number):
    for j in range(number*2-1):
        list[j].append('*')
        print (list)

print (list)