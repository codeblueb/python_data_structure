import timeit
import time

def bitwise_addition(a:int, b:int) -> int:
    """
        &    AND         sets each bit to 1 only if a and b are both 1
        ^    XOR         this adds the two numbers and returns 1 if bits are different
        <<   LEFT SHIFT  this adds the carry to the next higher-order bit poistion 
    """
    
    while b != 0:
        carry = a & b
        print(carry)
        a = a ^ b
        print(a)
        b = carry << 1
        print(b)
        print('----')
    return a

def arithmatic_addition(a:int, b:int) -> int:
    return a + b

def benchmark(func, a:int, b:int, iterations:int=1000000) -> float:
    statement = f"{func.__name__} ({a}, {b})"
    setup = f"from __main__ import {func.__name__}"

    time_taken = timeit.timeit(statement, setup, number=iterations)
    return time_taken

# a = 12345
# b = 789012
# Arithmatic addition time: 0.084263 seconds
# Bitwise addition time: 0.362502 seconds

# a = 123456789
# b = 1987654321
# Arithmatic addition time: 0.082730 seconds
# Bitwise addition time: 0.528143 seconds

# sol = bitwise_addition(91, 19)
# print(sol)

arithmatic_time = benchmark(arithmatic_addition, a, b)
print(f"Arithmatic addition time: {arithmatic_time:.6f} seconds")


bitwise_time = benchmark(bitwise_addition, a, b)
print(f"Bitwise addition time: {bitwise_time:.6f} seconds")

