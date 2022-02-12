

def binary_search(n,a):
    #initialize left and right 
    left = 0
    right = len(n)-1

    #loop thought the length divided by 2
    for i in range (len(n)//2): 

        #calculate midspan  
        x = (right + left) // 2
        #return index if it has the same value 
        if (a == n[x]):
            return x
        #change the left position if value is greater than midspan
        elif a > n[x]:
            left = x + 1
        #change right part if value is lower than midspan 
        elif a < n[x]:
            right = x - 1
    #return -1 if its not there 
    return -1



#get user input 
y = int(input("input a number: " ))

#return the index 
print(f"the index is {binary_search(x,y)}")