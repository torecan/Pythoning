#!/usr/bin/env python

import math
import cgi
import wsgiref.handlers
import os

def perfc(num):
    suma=0
    i=0
    for i in range(int(num)):
        if i==0:
            continue
        else:
            if (num%i==0) :
                print(i)
                suma+=i

    if (suma==num):
        print("PERFECT")
    else:
        print("NOT PERFECT")
            



a= input("Gir: ")
perfc(int(a))
