# -*- coding: utf-8 -*-
"""BondPrice_Z_File

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1G-LpGxAiewpGbv-Vfqt0epoVd7hqIGMp
"""

def getBondPrice_Z(face, couponRate, times, yc):
    coupon = face * couponRate
    bondPrice = 0

    for t, rate in zip(times, yc):
        bondPrice += coupon / ((1 + rate) ** t)

    bondPrice += face / ((1 + yc[-1]) ** times[-1])
    return bondPrice

yc = [.010,.015,.020,.025,.030]
times=[1,1.5,3,4,7]
face = 2000000
couponRate = .04

print("Bond Price with Zip YC:", getBondPrice_Z(face, couponRate, times, yc))