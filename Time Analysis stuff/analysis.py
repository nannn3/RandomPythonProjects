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
    '''
    

    Parameters
    ----------
    func : Function
        the function to be timed
    *kwargs : optional
        d: return the data along with the time it takes to run in the form (data,time).

    Returns
    -------
    Int
        time taken to run a function.

    '''
    #pdb.set_trace()
    if 'd' in kwargs:
        @wraps(func)
        def wrap(*args,**kwargs):
            start=time.time()
            ans=func(*args,**kwargs)
            stop=time.time()
            return ans,stop-start
    else:
        @wraps(func)
        def wrap(*args, **kwargs):
            start=time.time()
            func(*args, **kwargs)
            stop=time.time()
            return stop-start
    return wrap




@timer('d')
def test(n):
   # pdb.set_trace()
    ans=0
    for i in range(n):
        ans+=i
    return ans
        
if __name__=="__main__":
    print(test(10**6))