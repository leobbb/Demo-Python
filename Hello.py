#!/usr/bin/env python

import sys

def Hello(name):
  if name == 'Alice' or name == 'Nick' :
    print 'Alice: Alice Mode'
    name = name + '???'
  else:
    print 'Else'
  name = name + '!!!'
  print 'Hello', name


def main():
  Hello(sys.argv[1])


if __name__ == '__main__' : 
  main()


