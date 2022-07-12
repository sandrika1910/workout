def collatz(n,counter=0):
    if n == 1:
        return counter
    elif n % 2:
        return collatz(n * 3 + 1,counter + 1)
    else:
        return collatz(n/2,counter + 1)
   
print(collatz(7))

