import numpy as np
import cv2
import pytesseract
from PIL import Image
from pprint import pprint

img = cv2.imread('sudoku.png',0)
small=cv2.resize(img,(450,450))
puzzle = []
for i in range(0,9):
	y1 =50*i 
	y2 =50*(i+1)
	row = []
	for j in range(0,9):
		x1 = 50*j
		x2 = 50*(j+1)
		roi =small[y1:y2, x1:x2]
		roi = roi[3:48,3:48] # to clean out the borders
		content_img = Image.fromarray(roi)
		content = pytesseract.image_to_string(content_img, config='--psm 10')
		row.append(content)
	puzzle.append(row)
pprint(puzzle)
##TODO: solve the sudoku
cv2.imshow('image',small)
cv2.waitKey(0)
cv2.destroyAllWindows()
