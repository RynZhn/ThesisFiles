
# Python program to create  
# a file explorer in Tkinter 
   
# import all components 
# from the tkinter library 
from tkinter import *
   
# import filedialog module 
from tkinter import filedialog 

dataFile = None
sqrlFile = None
wtcFile = None


# Function for opening the  
# file explorer window 
def selectData(): 
    filename = filedialog.askopenfilename(initialdir = "../Data", 
                                          title = "Select a File", 
                                          ) 
    print(filename)
    global dataFile
    dataFile = filename
       
def selectSqrl(): 
    filename = filedialog.askopenfilename(initialdir = "../Data", 
                                          title = "Select a File", 
                                          ) 
    global sqrlFile
    sqrlFile = filename

def selectWTC(): 
    filename = filedialog.askopenfilename(initialdir = "../Data", 
                                          title = "Select a File", 
                                          ) 
    global wtcFile
    wtcFile = filename

                                                                                                   
# Create the root window 
window = Tk() 
   
# Set window title 
window.title('File Explorer') 
   
# Set window size 
window.geometry("500x500") 
   
#Set window background color 
window.config(background = "white") 
   
# Create a File Explorer label 
label_file_explorer = Label(window,  
                            text = "File Explorer using Tkinter", 
                            width = 100, height = 4,  
                            fg = "blue") 
   
       
button_data = Button(window,  
                        text = "Select Data File", 
                        command = selectData)  

button_sqrl = Button(window,
                        text = "Select Squirrel File",
                        command = selectSqrl)

button_wtc = Button(window,
                        text = "Select Squirrel File",
                        command = selectWTC)
button_exit = Button(window,  
                     text = "Done", 
                     command = window.destroy)  
   
# Grid method is chosen for placing 
# the widgets at respective positions  
# in a table like structure by 
# specifying rows and columns 
label_file_explorer.grid(column = 1, row = 1) 
   
button_data.grid(column = 1, row = 2) 

button_sqrl.grid(column = 1, row = 3)

button_wtc.grid(column = 1, row = 4)
   
button_exit.grid(column = 1,row = 5) 
   
# Let the window wait for any events 
window.mainloop() 
