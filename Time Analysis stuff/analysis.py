from functools import wraps,partial
import time
import pdb
import matplotlib.pyplot as plt

def doublewrap(f):
    '''
    a decorator decorator, allowing the decorator to be used as:
    @decorator(with, arguments, and=kwargs)
    or
    @decorator
    '''
    @wraps(f)
    def new_dec(*args, **kwargs):
        if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
            # actual decorated function
            return f(args[0])
        else:
            # decorator arguments
            return lambda realf: f(realf, *args, **kwargs)

    return new_dec

@doublewrap
def timer(func, *kwargs):
    
    @wraps(func)
    def wrap(*args, **kwargs):
        start=time.time()
        ans=func(*args, **kwargs)
        stop=time.time()
        return stop-start
    return wrap




@timer()
def test(n):
   # pdb.set_trace()
    ans=0
    for i in range(n):
        ans+=i
    return ans
        
if __name__=="__main__":
    print(test(10**6))