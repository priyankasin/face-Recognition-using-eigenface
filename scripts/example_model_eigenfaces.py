import sys
import numpy as np
from pylab import *
from PIL import Image
from io import StringIO
# append tinyfacerec to module search path
sys . path . append ("..")


# import tinyfacerec modules
from tinyfacerec . util import read_images

from tinyfacerec . model import EigenfacesModel
from scripts . data_spilt import data_spilts
# read images

data_spilts(train=5)
[X,y] = read_images ("/home/priyanka/Desktop/scripts/Test")

[A,a] = read_images ("/home/priyanka/Desktop/scripts/Train")

model = EigenfacesModel (X[0:] , y [0:])

correct=0
incorrect=0
for i in range(size(a)):
	if a[i] ==model . predict (A[i]):
		correct+=1
	else:
		incorrect+=1
print("Correct = ",correct)
print("Incorrect = ",incorrect)
Accuracy=(size(a)-incorrect)*100/size(a)
print("Accuracy is :", Accuracy)

