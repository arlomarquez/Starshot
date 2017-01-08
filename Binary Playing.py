import binascii as bin
import functools
import numpy as py
import random as rand
from PIL import Image

def semirandom_array(n):
	span = 255
	
	b = 0
	
	r = py.empty(n, dtype = int)

	for a in range(n):
	
		if b > span:
			b = 0

		r[a] = b

		b = b + 1

	return r

def length8_binarray(n):
	r= py.empty(n,dtype = bin)
	b = True
	for a in range(n):
		if b:
			r[a] = 00000000
			b = False
		else:
			r[a] = 11111111
			b = True
	return r


# img = Image.new( 'RGB', (2000,1000), "black") # create a new black image
# pixels = img.load() # create the pixel map

# for i in range(img.size[0]):    # for every pixel:
#     for j in range(img.size[1]):
#         pixels[i,j] = (first_5, last_3 + first_3, last_5) # set the colour accordingly

# img.save("example.png")

