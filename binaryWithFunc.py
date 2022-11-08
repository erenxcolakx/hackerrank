
import math
import os
import random
import re
import sys
n = int(input().strip())

def decimalToBinary(n):
    if n >=1:
        decimalToBinary(n//2)
    print(n % 2 , end="" )
decimalToBinary(n)