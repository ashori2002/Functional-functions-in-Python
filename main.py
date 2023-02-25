
myList = [1,2,3,4,5,6,7]
"""
def mines(num):
    num -= 1
    return num
myList_new = list(map(mines,myList))

print(myList_new)
"""

myList_new = list(map(lambda num : num - 1 , myList))

print(myList_new)

###################################################################
"""
def odd(num):
    return num % 2 == 0
myList_new1 = list(filter(odd , myList))
"""
myList_new1 = list(filter(lambda num : num % 2 == 0 , myList))
print(myList_new1)