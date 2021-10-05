#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 14:56:55 2021

@author: June Knauth
"""

# Derived from "graphing demo", version 20210902, 16:46, hmh

#Imports
import numpy as np
import matplotlib.pyplot as plt

# construct an array of values of h, ranging from 1 down to 10^-18, by factors
# of 10
exponents=np.linspace(0,18,19)    # the array [0, 1, 2, ..., 18]
h=10**(-exponents)                # the array [1, 0.1, 0.01, ..., 10^-18]


# These functions are passed the array h and the x value and return the error
# of each formula

# I guess in theory this could all be one function, but it would have
# a bunch of conditionals anyway, since the formulae are hardcoded

def error_2pt(x, delta_x):
    # compute the error in the derivative of x^5, by comparing the analytical
    # result with the result using the 2-point formula
    error_in_deriv=abs(5*x**4-
                       ((x+delta_x)**5-(x)**5)/(delta_x))
    return(error_in_deriv)


def error_3pt(x, delta_x):
    # compute the error in the derivative of x^5, by comparing the analytical
    # result with the result using the 3-point formula
    error_in_deriv=abs(5*x**4-
                       ((x+delta_x)**5-(x-delta_x)**5)/(2*delta_x))
    return(error_in_deriv)

def error_5pt(x, delta_x):
    # compute the error in the derivative of x^5, by comparing the analytical
    # result with the result using the 5-point formula
    error_in_deriv=abs(5*x**4-
                      (-1*(x+(2*delta_x))**5
                       +8*(x+delta_x)**5
                       -8*(x-delta_x)**5
                       +(x-(2*delta_x))**5)
                       /(12*delta_x))
    return(error_in_deriv)

## An alternate, iterative approach I added to test how fast the nparray
## method was- it takes 172us to numpy's 27

# def alt_error_5pt(x, delta_x):
#     error_in_deriv = []
#     for i in delta_x:
#         error_in_deriv.append(abs(5*x**4-
#                       (-1*(x+(2*i))**5
#                         +8*(x+i)**5
#                         -8*(x-i)**5
#                         +(x-(2*i))**5)
#                         /(12*i)))
#     return error_in_deriv
        

# I'm using an array to store the errors, mostly because I don't want to write
# three variable names

# If I were going to generalize this I would probably use a 
# dict just so it was clear which was which, and rewrite the above funcs
# into one function that calculates the forumlae on demand

errors = [0]*3 # Initialize the array. errors.append() would also work
errors[0] = error_2pt(2,h) # Calculate each error. They're passed nparray h 
errors[1] = error_3pt(2,h) # so the calculations are done element-wise and
errors[2] = error_5pt(2,h) # the result is also an nparray. numpy magic!
# Out of interest I checked and it's fast, too- more than 6 times faster than
# an iterative approach with a for loop.

#alt_error = alt_error_5pt(2, h) # the alternate function
print(h)
print(errors)

plt.plot(h, errors[0], label='2pt') # adds each result to the plot with a label
plt.plot(h, errors[1], label='3pt')
plt.plot(h, errors[2], label='5pt')
plt.xscale('log') # log axes and add proper graph sizes
plt.xlim([1, 1.e-16])
plt.yscale('log')
plt.ylim([1.e-12, 100])
plt.grid()
plt.title("Error graph for various numerical derivative approximations")
plt.xlabel("h (log scale)")
plt.ylabel("Error (log scale)")
plt.legend() # show the labels
plt.show() # render plot