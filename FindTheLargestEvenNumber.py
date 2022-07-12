# def f(l,n,k):
#     if l[n] % 2 == 0 and l[n] > k:
#         k=l[n]
#     if n == 0:
#         return k  
#     return f(l,n-1,k)

# print(f([1,2,8,10,13,24,5],6,-1))

def f(l,n,k,counter):
    if l[n] > k:
        k=l[n]
    if n == 0:
        counter += 1
        print('counter',counter)
        return k  
    counter+=1 
    print('counter: ', counter)
    return f(l,n-1,k,counter)

print(f([1,2,8,10,13,3,24],6,-1,0))


