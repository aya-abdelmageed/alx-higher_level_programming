#!/usr/bin/python3

def uniq_add(my_list=[]):
   x = []
   sum = 0
   for i in my_list:
      if i not in x:
         sum += i
         x.append(i)
   return sum
