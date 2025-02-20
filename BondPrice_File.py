# -*- coding: utf-8 -*-
"""BondPrice_File

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1h5QBmGdTpCc-Up3vXaA_42m6c395BYXp
"""

def getBondPrice(y, face, couponRate, m, ppy=1):
  df0=1/(1+y/ppy)
  dcf=0
  df=1
  bondPrice=0
  cpn=couponRate*face/ppy
  for i in range(1,m*ppy+1):
    df*=df0
    dcf+=cpn*df
  bondPrice=dcf+face*df

  return(bondPrice)

y = 0.03
face = 2000000
couponRate = 0.04
m = 10
#ppy = 1
ppy = 2

print("Bond Price:", getBondPrice(y, face, couponRate, m, ppy))