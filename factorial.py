#def factorial(num):
#    # Base case
#    if num == 1:
#        return num
#    else:
#        return num * factorial(num - 1)
#
#print(factorial(5))

''' is the input Factorial of an integer? '''

def isFactorial(num,k,b):
    if k == num:
        return True
    elif k < num:
        k = k * b
        #print(k)
        return isFactorial(num,k,b+1)
    else:
        return False
print(isFactorial(9,1,1))
