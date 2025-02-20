# -*- coding: utf-8 -*-
"""FizzBuzz_File

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DtCVT7GJVN9SfZ0oTZGXcMVNkLL3HbiK
"""

def FizzBuzz(start, finish):
    outlist = []
    for i in range(start, finish + 1):
        if i % 15 == 0:
            outlist.append("fizzbuzz")
        elif i % 3 == 0:
            outlist.append("fizz")
        elif i % 5 == 0:
            outlist.append("buzz")
        else:
            outlist.append(str(i))
    return outlist

print("FizzBuzz Output:" ,FizzBuzz(40, 45))