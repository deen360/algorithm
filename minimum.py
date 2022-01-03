
arr = [10, 20, 30, 50, 70, 12, 0.5, 2, 10]

#counts the number of elements in array 
num = len(arr)

def mini(num, array):
    #initialize the first element in the array
    min = array[0]
    
    #iterates through the array to find minimum value 
    for i in range(num):
        if min > array[i]:
            min = array[i]
    return min

print(mini(num, arr))