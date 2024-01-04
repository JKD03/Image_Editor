import random
import tkinter as tk
from tkinter import filedialog
from tkinter import  colorchooser
import customtkinter as ctk
from customtkinter import *
from PIL import Image,ImageOps,ImageTk,ImageFilter

# button1="cyan"
button_text = "white"
root=ctk.CTk()
root.geometry("1000x600")
root.title("Image Editor")


pen_color="black"
pen_size=5
file_path=""

theme_color="Dark"
themes1=["blue","green","dark-blue"]
# set_default_color_theme("blue")
set_appearance_mode("System")

def add_image():
    global file_path
    file_path=filedialog.askopenfilename(initialdir=r"/C:\Users\talk2\OneDrive\Pictures")
    image=Image.open(file_path)
    width,height=int(image.width/2),int(image.height/2)
    image=image.resize((width,height),Image.ANTIALIAS)
    canvas.config(width=image.width,height=image.height)
    image=ImageTk.PhotoImage(image)
    canvas.image = image
    canvas.create_image(0,0,image=image,anchor="nw")

def draw(event):
    x1,y1=(event.x-pen_size),(event.y-pen_size)
    x2,y2=(event.x+pen_size),(event.y+pen_size)
    canvas.create_oval(x1,y1,x2,y2,fill=pen_color,outline='')

def change_color():
    global pen_color
    pen_color=colorchooser.askcolor(title="Select Color")[1]

def update_pen_size(value):
    global pen_size
    pen_size = int(value)

def clear_canvas():
    canvas.delete("all")
    addimg()
def clear_canvas_all():
    canvas.delete("all")
def addimg():
    canvas.create_image(0, 0, image=canvas.image, anchor="nw")

def apply_filter(filter):
    image=Image.open(file_path)
    width,height=int(image.width/2),int(image.height/2)
    image=image.resize((width,height),Image.ANTIALIAS)
    if filter=="Orignal":
        None
    elif filter=="Black and White":
        image=ImageOps.grayscale(image)
    elif filter=="Blur":
        image=image.filter(ImageFilter.BLUR)
    elif filter=="Sharpen":
        image=image.filter(ImageFilter.SHARPEN)
    elif filter=="Smooth":
        image=image.filter(ImageFilter.SMOOTH_MORE)
    elif filter=="Emboss":
        image=image.filter(ImageFilter.EMBOSS)
    elif filter=="Mirror":
        image=ImageOps.mirror(image)
    elif filter=="Auto Contrast":
        image=ImageOps.autocontrast(image, cutoff=0, ignore=None)
    elif filter=="Contour":
        image = image.filter(ImageFilter.CONTOUR)
    elif filter=="Boundary Enhance":
        image = image.filter(ImageFilter.EDGE_ENHANCE)


    image=ImageTk.PhotoImage(image)
    canvas.image=image
    canvas.create_image(0,0,image=image,anchor="nw")

def theme_change():
    global theme_color
    if theme_color=="light":
        theme_color="Dark"
    else:
        theme_color="light"
    set_appearance_mode(theme_color)


addimg=Image.open('add.png')
penimg=Image.open('pen.png')
binimg=Image.open('bin.png')
left_frame = ctk.CTkFrame(root)
left_frame.pack(side="left",expand=True,padx=20,pady=20)
canvas = tk.Canvas(root,width=750,height=600,bg="#303030",bd=0,highlightthickness=0)
canvas.pack(side="left",padx=20,pady=0)

image_button = ctk.CTkButton(left_frame, text="Add Image", command=add_image)
image_button.grid(row=0,column=0,columnspan=2,sticky="news",padx=10,pady=10)

color_button = ctk.CTkButton(left_frame, text="Change Pen Color", command=change_color,image=CTkImage(dark_image=penimg))
color_button.grid(row=1,column=0,columnspan=2,sticky="news",padx=10,pady=10)

pen_size_frame = ctk.CTkFrame(left_frame)
pen_size_frame.grid(row=2,column=0,columnspan=2,sticky="news",padx=10,pady=10)
pen_size_1 = ctk.CTkSlider(pen_size_frame, from_=1, to=300, command=update_pen_size,hover=True,progress_color='#2179bc')
pen_size_1.pack(side="left")

filter_label = ctk.CTkLabel(left_frame, text="Select Filter")
filter_label.grid(row=3,column=0,padx=10,pady=10)
filters = ["Orignal", "Black and White", "Blur", "Emboss", "Sharpen", "Smooth", "Mirror", "Auto Contrast", "Contour",
           "Boundary Enhance"]
filter_combox = ctk.CTkComboBox(left_frame, values=filters)
filter_combox.set("Original")
filter_combox.grid(row=3,column=1,padx=10,pady=10)

clear_button = ctk.CTkButton(left_frame, text="Clear", command=clear_canvas,image=CTkImage(dark_image=binimg))
clear_button.grid(row=4,column=0,columnspan=2,sticky="news",padx=10,pady=10)

clear_all = ctk.CTkButton(left_frame, text="Clear All", command=clear_canvas_all,image=CTkImage(dark_image=binimg))
clear_all.grid(row=5,column=0,columnspan=2,sticky="news",padx=10,pady=10)

thememode = ctk.CTkButton(left_frame,text="Change Theme",command=theme_change)
thememode.grid(row=6,column=0,columnspan=2,sticky="news",padx=10,pady=10)

filter_combox.bind("<<ComboboxSelected>>",lambda event: apply_filter(filter_combox.get()))

canvas.bind("<B1-Motion>",draw)
root.mainloop()