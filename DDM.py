#!/usr/bin/python
import sys
import math

def CalDDM(divi, diviGrowth, profit):
   value = float(0)
   diviCal = float(0)
   diviGrowthCal = float(0)
   profitCal = float(0)
   print ('divi: %f' %divi)
   print ('diviGrowth: %f' %diviGrowth)
   print ('profit: %f' %profit)
   for x in range(1,40):
      diviGrowthCal = math.pow((1 + diviGrowth), x)
      profitCal = math.pow((1 + profit), x)
      diviCal = (divi * diviGrowthCal) / profitCal
      value = diviCal + value
   print ('Now Value: %f' %value)

def main():
   divi = float(input('Input dividend:\n'))
   diviGrowth = float(input('Input dividend Growth%:\n'))
   profit = 0.1
   CalDDM(divi, diviGrowth, profit)

if __name__=='__main__':
   main()
