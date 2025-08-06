#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

user_input = ''
file_header = ''
exnum = 0
fnum = 0
min_cmap = 0
max_cmap = 100

def show_keck(dta, fignum):
	#display the image in dta
	fig = plt.figure(num=fignum,figsize=(6.67,4.),dpi=150)
	plt.clf()
	ax1 = fig.add_subplot(111)
	dtaimg = ax1.imshow(dta, vmin = min_cmap, vmax = max_cmap,cmap='bone')
	plt.axis('off')
	cbar =fig.colorbar(dtaimg,ax=ax1)
	cbar.ax.tick_params(labelsize=8)
	cbar.set_label('[ADU]',rotation=270,size=8)
	plt.show()

def single():
	img = Image.open(file_header + '_' + time  + exposure + '_00000_' + frame + '.tif', 'r')
	arr = np.array(img)
	img.close()
	show_keck(arr, 1)

def multiple_frames():
	for exposure in range(first, last + 1):
		img = Image.open(file_header + '_' + time + str(exposure) + '_00000_' + frame + '.tif', 'r')
		arr = np.array(img)
		img.close()
		show_keck(arr,1)

def full_image():
	for frame in range(8):
		img = Image.open(file_header + '_' + time + exposure + '_00000_' + str(frame) + '.tif', 'r')
		arr = np.array(img)
		img.close()
		show_keck(arr,1)

def manual(file):
	img = Image.open(file, 'r')
	arr = np.array(img)
	img.close()
	show_keck(arr,1)

print('')
print('WELCOME TO TIF OPENER!')
print('BY N.W. Deelman')
print('')
print('------------------------')

print('')
print('COMMANDS:')
print('header - changes the file header (run if using single, multiple, or full')
print('single - opens a single image')
print('multiple - opens a group of images of the same frame and exposure time')
print('full - opens all 8 frames off an image')
print('manual - manually enter a file name')
print('color - changes the color scale')
print('')
print('------------------------')

while user_input != 'q':
	print('>', end='')
	user_input = input()
	if user_input == 'single':
		time = input('EXPOSURE TIME: ')
		exposure = input('EXPOSURE NUMBER: ')
		frame = input('FRAME NUMBER: ')
		single()
	if user_input == 'multiple':
		time = input('EXPOSURE TIME: ')
		frame = input('FRAME NUMBER: ')
		first = int(input('STARTING EXPOSURE: '))
		last = int(input('ENDING EXPOSURE: '))
		multiple_frames()
	if user_input == 'manual':
		file_name = input('FILENAME: ')
		manual(file_name)
	if user_input == 'full':
		time = input('EXPOSURE TIME: ')
		exposure = input('EXPOSURE NUMBER: ')
		full_image()
	if user_input == 'color':
		min_cmap = int(input('MINIMUM: '))
		max_cmap = int(input('MAXIMUM: '))
	if user_input == 'header':
		file_header = input('FILE HEADER: ')
	if user_input == 'q':
		break
	else:
		continue
	print('')
print('------------------------')
print('')
print('COME AGAIN SOON :)')
print('')



