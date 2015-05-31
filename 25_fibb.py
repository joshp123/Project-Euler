def fib(a, b):
    return b, a + b

def main():
    thousand_digits = 10**999
    a = 1
    b = 1
    last, fibb = fib(a, b)
    count = 3
    while (fibb < thousand_digits):
        last, fibb = fib(last, fibb)
        count += 1
    print("1k digits index: {}".format(count))
    print(fibb)

if __name__ == "__main__":
    main()
