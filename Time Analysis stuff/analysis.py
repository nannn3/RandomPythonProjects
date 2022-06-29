from functools import wraps,partial
import time
import pdb
def timer(*args,**kwargs):
    pdb.set_trace()
    no_args = False
    if len(args) == 1 and not kwargs and callable(args[0]):
        # We were called without args
        func = args[0]
        no_args = True
        def outer(func):
            @wraps(func)
            def withVals(*args):
                start=time.time()
                func(*args)
                end=time.time()
                return func(*args),end-start
            return withVals
        if no_args==True:
            return outer(func)
        else:
            return outer
@timer(1)
def test(n):
    ans=[]
    for i in range(n):
        ans.append(i**i)
    return ans
        
if __name__=="__main__":
    n=5
    print(test(n))
        