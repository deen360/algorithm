def linear_sort(a, y):
    #iterate through the length of the array
    for i in range (len(a)):
        #if an element in a is equal to y, return its index
        if (a[i] == y):
            return i
    #return a negative number if it cant be found 
    return -1

x = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]

#get user input 
p = int(input("input search number: "))

#return the index 
print(f"the index is {linear_sort(x, p)}")