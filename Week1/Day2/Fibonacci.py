#Function that returns the fibonacci sequence 

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)
#print(fibonacci(7))  
for x in range(12):
    print(fibonacci(x))