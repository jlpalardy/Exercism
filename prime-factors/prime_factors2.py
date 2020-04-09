def factors(value):
    if value <= 1:
        return []
    factor_list = []
    current = value
    while not current % 2:
        factor_list.append(2)
        current = int(current/2)
    divisor = 3
    while divisor <= current:
        while not current % divisor:
            current = int(current/divisor)
            factor_list.append(divisor)
        divisor += 2
    return factor_list
		

print(f'Prime factors of 2: {factors(2)}')
print(f'Prime factors of 1: {factors(1)}')
print(f'Prime factors of 0: {factors(0)}')
print(f'Prime factors of 8: {factors(8)}')
print(f'Prime factors of 12: {factors(12)}')
print(f'Prime factors of 36: {factors(36)}')
print(f'Prime factors of 123468960: {factors(123468960)}')
