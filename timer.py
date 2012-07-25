def func1():
    for x in xrange(50):
        result = x**0.5
        is_int = (int(result) == result)


def func2():
    for x in xrange(50):
        result = x**0.5
        is_int = (result % 1 == 0)


if __name__ == '__main__':
    from timeit import Timer

    t = Timer('func1()', 'from __main__ import func1')
    print 'func1', t.timeit()

    t = Timer('func2()', 'from __main__ import func2')
    print 'func2', t.timeit()