#!/usr/bin/env python

from PIL import Image
import sys, os

if len(sys.argv) > 2:
	image = sys.argv[1]
	magnitude = int(sys.argv[2])
	
else:
	image = raw_input("enter the name of the image file you would like to sketch: ")
	magnitude = int(input("enter the magnutide: "))
	
im = Image.open(image)
width =  im.size[0]
height = im.size[1]
picture = im.load()
for y in range(1,height):
	for x in range(1,width):
		if abs(sum(picture[x,y]) - sum(picture[x-1,y-1])) >= magnitude:
			im.putpixel((x-1,y-1), (0,0,0))
		elif abs(sum(picture[x,y]) - sum(picture[x-1,y])) >= magnitude:
			im.putpixel((x-1,y-1), (0,0,0))
		elif abs(sum(picture[x,y]) - sum(picture[x,y-1])) >= magnitude:
			im.putpixel((x-1,y-1), (0,0,0))
		else:
			im.putpixel((x-1,y-1),(255,255,255))


im.save('sketch.png')

