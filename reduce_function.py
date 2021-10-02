
import functools

def larg(a,b):
    return a if a>b else b

ls = [10, 20, 450, 21, 41.33, 617, 200]
print("main area starts")

ans = functools.reduce(larg,ls)

print("Sum of all elements is : ", ans)
print("main ends here")
