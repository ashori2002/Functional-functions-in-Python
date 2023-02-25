
myList = [1,2,3,4,5,6,7]
def mines(num):
    num -= 1
    return num
myList_new = list(map(mines,myList))

print(myList_new)