#!/usr/bin/env python3
from collections import Counter
def putInList(args, remove):
  f = open("english.txt","r")
  lista = []
  for line in f:
    if len(line) == 6:
      lista.append(line.replace("\n", "")) 
  f.close()
  l = []
  asd = []
  for i in lista:
    for j in remove:
      if j in i:
        asd.append(i)
  for i in asd:
    if i in lista:
      lista.remove(i)
  for i in lista:
    temp = not Counter(args) - Counter(i)
    if temp == True:
      l.append(i)
  print(len(l))
  print(l)
  
putInList("ayre", "tsduiophcnm")





