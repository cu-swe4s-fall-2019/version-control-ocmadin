import warnings

def div(a, b):
    """Divides a number 'a' by another number 'b'
    
    Parameters
    ----------
        a: int or float
            Number to be divided
        b: int or float
            Number to divide by
    Returns
    -------
        d: int or float
            Result of the division
    """
    
    if b == 0:
        warnings.warn('Division by 0 is not possible, returning "None"')
        d = None
    else:
        d = a/b
    return d
