#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import sqrt

# =================
print(">> Task 7")


class Complex(object):
    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real,
                       self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real,
                       self.imag - other.imag)

    def __mul__(self, other):
        return Complex(self.real*other.real - self.imag*other.imag,
                       self.imag*other.real + self.real*other.imag)

    def __div__(self, other):
        sr, si, o_r, oi = self.real, self.imag, \
                         other.real, other.imag # short forms
        r = float(o_r**2 + oi**2)
        return Complex((sr*o_r+si*oi)/r, (si*o_r-sr*oi)/r)

    def __abs__(self):
        return sqrt(self.real**2 + self.imag**2)

    def __neg__(self):   # defines -c (c is Complex)
        return Complex(-self.real, -self.imag)

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return '(%g, %g)' % (self.real, self.imag)

    def __repr__(self):
        return 'Complex' + str(self)

    def __pow__(self, power):
        raise NotImplementedError("Power is not yet impl. for Complex")


complex_num_1 = complex(1.0, 2.0)
print(f"First complex number: {complex_num_1}")
complex_num_2 = complex(1.0, 2.0)
print(f"Second complex number: {complex_num_2}")

print(f"Sum of complex numbers: {complex_num_1 + complex_num_2}")
print(f"Product of complex numbers: {complex_num_1 * complex_num_2}")

print("It's all done")

"""
===============================================================================
PS  I am very Grateful to you for the useful tips and hints on my code verification!
===============================================================================
"""
