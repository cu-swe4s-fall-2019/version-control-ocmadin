#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math_lib import add,div
import argparse

def add_divide(a,b,c):
    """ Calculates the sum of two numbers and divides them by a third
    
    Parameters
    ----------
    
    a,b: int
        numbers added together
    c:  int
        number to divide the first two by
    Returns
    -------
    d: float
        result of the computation
    """
    s = add(a,b)
    
    d = div(s,c)
    
    return d 

def main():
    parser = argparse.ArgumentParser(description='Process some input numbers')
    
    parser.add_argument('--first_number','-a',
                        type=int,
                        help='First integer to be added',
                        required=True)

    parser.add_argument('--second_number','-b',
                        type=int,
                        help='Second integer to be added',
                        required=True)

    parser.add_argument('--third_number','-c',
                        type=int,
                        help='Integer to divide by',
                        required=True)        
    
    args = parser.parse_args()
    print(args.first_number,args.second_number,args.third_number)
    d = add_divide(args.first_number,args.second_number,args.third_number)
    print(d)
    
if __name__ == '__main__':
    main()