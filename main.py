def fibonacci(n):
    if n < 0: raise ValueError(f'Fibonacci parameter must be greater than 0. Value received: {n}')

    if n == 0: return 0
    if n == 1: return 1
    return fibonacci(n - 2) + fibonacci(n - 1)

def salute(hour, name):
    if name == "" or name is None:
        raise ValueError(f'\'name\' parameter must not be empty')
    if hour < 0 or hour >= 24:
        raise ValueError(f'\'hour\' parameter must be >= 0 and < 24')
    

    if hour < 12:
        return f'Good Morning, {name}!'
    if hour < 18:
        return f'Good Afternoon, {name}!'
    else:
        return f'Good Night, {name}!'
    
def isDuck(quacks, fly, swim, walk):
    if quacks and fly and swim and walk:
        return 'is a duck'
    elif fly and swim:
        return 'probably a goose'
    elif swim and walk:
        return 'Steve, for sure'
    else: return 'Have no idea'