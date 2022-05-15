#!/usr/bin/env python3
import re
import random

list_of_words = []

WORD_OF_THE_DAY = ""

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#print(f"{bcolors.HEADER}Warning: No active frommets remain. Continue?{bcolors.ENDC}")

def load_list():
  f = open("lista.txt", 'r')
  for line in f:
    if bool(re.search('^[a-zA-Z0-9]*$',line))==True:
      list_of_words.append(line.replace("\n", ""))

load_list()

WORD_OF_THE_DAY = random.choice(list_of_words) 
print(WORD_OF_THE_DAY)


def filter_the_word(args):
  l = []
  for i in list_of_words:
    temp = not Counter(args) - Counter(i)
    if temp == True:
      l.append(i)

def guess_the_word(args):
  string1 ="" 
  for i in range(len(WORD_OF_THE_DAY)):
    if args[i] == WORD_OF_THE_DAY[i]:
      string1 += bcolors.OKGREEN + args[i]
    elif args[i] in WORD_OF_THE_DAY:
      string1 += bcolors.WARNING + args[i]
    else:
      string1 += bcolors.FAIL + args[i]
  return string1
 # return True if args == WORD_OF_THE_DAY else False 
  
print(guess_the_word("audio"))
print(guess_the_word("crest"))
print(guess_the_word("nymph"))