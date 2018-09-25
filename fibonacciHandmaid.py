
print("This program prints n numbers in the Fibonacci sequence.")
n = int(input("Enter positive integer n: "))
curr = 0
prev = 1
    
for i in range(n+1):
    if curr >0:
        print(curr)
    curr, prev  = curr + prev, curr


        

    
