def fibonacci_sequence(n):
    fibonacci = [0, 1]
    
    while len(fibonacci) < n:
            
            anothernum = fibonacci[-1] + fibonacci[-2]
            fibonacci = fibonacci + [anothernum]

    return fibonacci[:n]