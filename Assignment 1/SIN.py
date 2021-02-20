def make_sin(partial_number):
    '''
    Returns the 9 digit SIN givin the first 8 digits using a specifed algorithm
    
    make_sin: Nat -> Nat 
    Requires 
        Must be a 8 digit natural number 
        Each digit in partial_number must be between 0 and 9 
        First digit cannot be 0
        
    Examples:
        make_sin(64075429) => 640754297
        make_sin(20980000) => 209800002
    '''
    _1 = (partial_number // 10000000)
    _2 = (partial_number // 1000000 % 10) * 2
    _3 = partial_number // 100000 % 10
    _4 = (partial_number // 10000 % 10) * 2
    _5 = partial_number // 1000 % 10
    _6 = (partial_number // 100 % 10) * 2
    _7 = partial_number // 10 % 10
    _8 = (partial_number % 10) * 2
    
    add_even = (_2 // 10) + (_2 % 10) + (_4 // 10) + (_4 % 10) + \
               (_6 // 10) + (_6 % 10) + (_8 // 10) + (_8 % 10)
    
    add_odd = _1 + _3 + _5 + _7
    
    add_total = add_even + add_odd
    
    last_digit = add_total % 10
    
    almost_value = 10 - last_digit
    
    final_value = (partial_number * 10) + (almost_value % 10)
    
    return final_value 