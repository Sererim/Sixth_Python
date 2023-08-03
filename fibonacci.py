# Fibonacci function
# fn = fn-1 + fn-2
# f0 = 0
# f1 = 1
# f2 = 1
# f3 = 2
# f4 = 3
def fibonacci() -> int:
    fn0 = 0
    fn1 = 1
    f = 0
    while True:
        yield f
        f = fn0 + fn1
        fn0 = fn1
        fn1 = f
    

if __name__ == "__main__":
    fib = fibonacci()
    for i in range(10):
        print(next(fib))
