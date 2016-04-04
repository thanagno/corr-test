#!/bin/ipython


import glob, os
import numpy as np
from numpy import *
import math
import mpmath
import numpy as np


def P_corr(xarray, yarray):
#	t000 = time.time()
	xmean = np.mean(xarray)
	ymean = np.mean(yarray)
	a1 = np.sum((xarray-xmean)*(yarray-ymean))
	a2 = np.sqrt(np.sum((xarray-xmean)**2)*np.sum((yarray-ymean)**2))
	return a1/a2


a = np.loadtxt("file",unpack=True)
	tt=a[0]
	ff=a[1]
	ee=a[2]

	Pe_coef = P_corr(tt, ff)
	file1 = open('object.txt', 'w')
	file1.write(str('%s\n') % (Pe_coef))
	file1.close()

exit()


