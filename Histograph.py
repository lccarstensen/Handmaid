#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 14:44:49 2018

@author: lucascarstensen
"""

import numpy as np
import matplotlib.pyplot as plt

M = np.random.randn(10,1000)
print(M)

M[M>0] = 1
print(M)

Q=np.matrix.flatten(M)

plt.hist(Q)
