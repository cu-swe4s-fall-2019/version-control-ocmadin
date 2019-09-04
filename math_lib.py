def div(a, b):
    """
    Divides a number 'a' by another number 'b'
    
    Parameters
    ----------
    a: int or float
        Number to be divided
    b: int or float
        Number to divide a by
    
    Returns
    -------
    d: int or float
        Result of the division between a and b
    """
    
    if b == 0:
        print('Error: cannot divide by 0')
        quit()
    
    d=a/b
    
    return d
