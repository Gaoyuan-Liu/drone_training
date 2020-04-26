#!/usr/bin/env python

x = float(input())
y = float(input())
if __name__ == '__main__':
    sn = calculate_state_number(x, y)
    print (sn)

def calculate_state_number(x, y):
    for i in range(10):
        if x >= -5+i and x < -5+i+1:
            numberx = 10 * i
    for j in range(10):
        if y >= -5+j and y < -5+j+1:
            numbery = j

    state_number = numberx + numbery
    return state_number

