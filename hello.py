def outer0(fun):
    print "start outer0"
    def inner(*a,**b):
        print "start inner0"
        ret = fun(*a,**b)
        print "end inner0"
        return ret
    print "end outer0"
    return inner

def outer1(fun):
    print "start outer1"
    def inner(*a,**b):
        print "start inner1"
        ret = fun(*a,**b)
        print "end inner1"
        return ret
    print "end oute1"
    return inner

@outer1
@outer0
def f1(a,b,w):
    print "function f1"
    # print a
    # print b
    # print type(w)
    # print w

# f1 = outer(f1)
f1(1,2,w=3)
