#FIBONACCI SEQUENCE

def fibonacci_sequence(n):
    a,b = 0,1
    for fibonacci_sequence in range(n):
        yield a
        a,b = b,a+b

print(list(fibonacci_sequence(15)))




