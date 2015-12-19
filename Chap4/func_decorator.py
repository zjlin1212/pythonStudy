__author__ = 'lin'

import time
def time_cost(timef):

    def function(f):
        def f1(*arg,**kwarg):
            start=timef()
            a=f(*arg,**kwarg)
            end=timef()
            print  f.__name__, "run cost time is ", end-start
            return a
        return f1

    return function

@time_cost(time.clock)
def for_loop(length):
    a=[]
    for x in range(0,length):
        for y in range(0,length):
            if x*y>25:
                a.append((x,y))


    return a
@time_cost(time.clock)
def list_loop(xlen,ylen):
    return [(x,y) for x in range(0,xlen) for y in range(0,ylen) if x*y>25]

def testfunc(*arg,**kwarg):
    print arg
    if kwarg['k']:
        print 'kwarg[k]=',kwarg['k']



if __name__=='__main__':
    a=for_loop(1000)
    b=list_loop(1000,1000)
    print len(a)
    print len(b)