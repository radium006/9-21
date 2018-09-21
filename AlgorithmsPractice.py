print("Welcoe to Kevin's Algorithm Practice Program")


def getLargestNum(arr): 
    largest = 0
    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    return largest

def getSmallestNum(arr):
    smallest = getLargestNum(arr)
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
    return smallest

def duplicates(arr):
    newArr = []
    for name in arr:
        if name not in newArr:
            newArr.append(name)
    return newArr

def triangle(x):
    spaces = x
    for i in range(0, x, 2):
        
        for j in range(0, spaces):
            print(end=" ")
        
        spaces -= 2

        for j in range(0, i+1):
            print("*", end=" ")
        print("\r")   
    return 
 



numArray = [8, -8, 9, 45, 88, 9, 767, 100, 676, -5666]
nameArray = ["Kevin" , "John", "Dom" , "Kevin" , "Joe" , "James" , "Joe", "James" , "Joe"]

print("The array of integers is: " + str(numArray))
print("The array of names is: " + str(nameArray))
print("The largest integer in the integer array is: " + str(getLargestNum(numArray)))
print("The smallest integer in the integer array is: " + str(getSmallestNum(numArray)))
print("Name array with duplicates deleted: " + str(duplicates(nameArray)))
triangle(30)