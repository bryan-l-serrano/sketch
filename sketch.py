#!/usr/bin/env python

from PIL import Image
import sys, os

if len(sys.argv) > 1:
	image = sys.argv[1]
else:
	image = raw_input("enter the name of the image file you would like to sketch")

im = Image.open(image)
width =  im.size[0]
height = im.size[1]
picture = im.load()
for y in range(1,height):
	for x in range(1,width):
		if abs(sum(picture[x,y]) - sum(picture[x-1,y-1])) >= 100:
			im.putpixel((x-1,y-1), (0,0,0))
		elif abs(sum(picture[x,y]) - sum(picture[x-1,y])) >= 100:
			im.putpixel((x-1,y-1), (0,0,0))
		else:
			im.putpixel((x-1,y-1),(255,255,255))


im.save('sketch.png')

