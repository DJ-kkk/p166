from tkinter import *
from PIL import ImageTk, Image


root= Tk()
root.title("Working on Canvas Using functions")
root.geometry("600x600")

canvas=Canvas(root, width = 990, height=490, bg = "white", highlightbackground="gray")
fillcolour=["green","yellow","red","blue"]
colour_dropdwon = ttk.Combobox(root,state="readonly" ,values = fillcolour, width = 10)
startx=Label(root,text="startx")
d1 = ttk.Combobox(root,state="readonly" ,values = coordinates_values, width = 10)
coordinates_values= [10,50,100,200,300,400,500,600,800,900]