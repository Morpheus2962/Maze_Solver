import numpy as np
import cv2
import matplotlib.pyplot as plt
from maze import find_shortest_path, drawPath
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

coords =[0,0,0,0]  
path = ''
def click_event(event, x, y, flags, params): 
    global path
    img = cv2.imread(path)
    if event == cv2.EVENT_LBUTTONDOWN: 
  
        #print(x, ' ', y) 
        cv2.circle(img, (x, y), 3, (0,255,0),-1)
        cv2.imshow('Maze', img) 
        coords[0] = x
        coords[1] = y
    if event==cv2.EVENT_RBUTTONDOWN: 
  
        #print(x, ' ', y) 
        cv2.circle(img, (x, y), 3, (0,255,0),-1)
        cv2.imshow('Maze', img)
        coords[2] = x
        coords[3] = y
        cv2.destroyAllWindows()
  
def open_img(): 
    global path
    path = openfilename() 

def openfilename(): 

    filename = filedialog.askopenfilename(title ='"pen') 
    return filename 
 
def solve():
    global path
    img = cv2.imread(path)
    cv2.imshow('Maze', img) 

    cv2.setMouseCallback('Maze', click_event) 

    cv2.waitKey(0) 

    cv2.destroyAllWindows() 
    #print(coords)

    image = img
    path = find_shortest_path(image,(coords[0], coords[1]),(coords[2], coords[3]))
    path_thickness = (image.shape[0]+image.shape[0])//2//125
    drawPath(image, path, path_thickness)
    cv2.imshow('Solved Maze', image)
    cv2.waitKey(0)





root = Tk()
root.title("Maze Solver")
root.configure(background = 'light blue')
root.geometry("400x250")
root.resizable(width = True, height = True)
text = "Select the Maze Image"
text1 = "After Clicking Solve " 
text2 = "Select Start point by Left Mouse click "
text3 = "Select End point by Right Mouse click "
label = Label( root, text=text, font = 10, bg = "light blue").place(x = 10, y = 10)
btn = Button(root, text = 'Open Image', command = open_img, height = 2, width = 20, bg = "light coral").place(x = 10, y = 70)
btn2 = Button(root, text = '    Solve    ', command = solve, height = 2, width = 20, bg = "light coral").place(x = 220, y = 70)
label = Label( root, text=text1, font = 10, bg = "light blue").place(x = 10, y = 150)
label = Label( root, text=text2, font = 10, bg = "light blue").place(x = 10, y = 180)
label = Label( root, text=text3, font = 10, bg = "light blue").place(x = 10, y = 210)

root.mainloop()

