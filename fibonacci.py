found = {0:0, 1:1, 2:1}

# returns the fibonacci of n
def fib(n):
    result = 0
    if n not in found:
        result = fib(n-1) + fib(n-2)
    else:
        result = found[n]
    return result

# some examples
def main():
    print("n: 3, fib: " + str(fib(3)))
    print("n: 30, fib: " + str(fib(30)))
    print("n: 15, fib: " + str(fib(15)))
    print("n: 25, fib: " + str(fib(25)))

main()