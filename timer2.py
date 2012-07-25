import random

def func1():
    array = []
    for x in xrange(10000):
        a = random.randint(1,10000)
        if a not in array:
            array.append(a)
    # print len(array)



def func2():
    array = []
    for x in xrange(10000):
        a = random.randint(1,10000)
        if array.count(a) <= 1:
            array.append(a)
    # print len(array)


if __name__ == '__main__':
    from timeit import Timer

    t = Timer('func1()', 'from __main__ import func1')
    print 'func1', t.timeit(number = 50)

    t = Timer('func2()', 'from __main__ import func2')
    print 'func2', t.timeit(number = 50)