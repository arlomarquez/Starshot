import numpy as py
import random as rand

def ascending_list(n):
	r = py.empty(n, dtype='string')
	span = 255
	b = -1

	for a in range(n):
		b = b + 1
		if b > span:
			b = 0
		s = str(bin(b)[2:])
		r[a] = str((8-len(s))*"0") + s
	return r
	
def random_list(n):
	r = py.empty(n, dtype='string')
	span = 255

	for a in range(n):
		b = randint(0,255)
		s = str(bin(b)[2:])
		r[a] = str((8-len(s))*"0") + s
	return r 

n = 3000000

asc_l = ascending_list(n)

r_sort = py.empty((n*3/2),dtype=tuple) #should have len()==4500000



k=0

for c in range(n):
	if (k<=(n*3/2-3)):
		r_sort[k] = (asc_l[c])[:4]
		r_sort[k+1] = (asc_l[c])[5:]+(asc_l[c+1])[:2]      #Might need to change
		r_sort[k+2] = (asc_l[c+1])[3:]
		c = c + 1
		k = k + 3

print asc_l[55]
print r_sort[55]



img = Image.new( 'RGB', (2000,1500), "black") # create a new black image
pixels = img.load() # create the pixel map

k=0
s = 0
for x in range(img.size[0]):    # for every pixel:
	for y in range(img.size[1]):
		pixels[x,y] = (int(r_sort[k]), int(r_sort[k+1]), int(r_sort[k+2])) # set the colour accordingly
		s = s + 1			
		if (k<=(len(r_sort)-3)):
				k = k + 3
		else:
			print 'donezo'
			print k
			print s
			break


img.save("example.png")
