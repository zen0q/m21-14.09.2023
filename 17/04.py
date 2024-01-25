def continue_fibonacci_sequence(sequence, n):
    for i in range(n):
        next_element = sequence[-1] + sequence[-2]
        sequence += [next_element]
    return sequence

sequence = [1, 1]
continue_fibonacci_sequence(sequence, 1)
print(*sequence)

print('*****')

sequence = [1, 1, 2, 3, 5]
continue_fibonacci_sequence(sequence, 0)
print(*sequence)
