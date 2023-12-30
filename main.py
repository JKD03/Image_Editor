import tkinter as tk
from tkinter import filedialog
from tkinter import  colorchooser
from PIL import Image,ImageOps,ImageTk,ImageFilter
from tkinter import ttk
from ttkthemes import ThemedStyle

button1="cyan"
button_text = "white"
root=tk.Tk()
root.geometry("1000x600")
root.title("Image Editor")
root.config(bg='white')

pen_color="black"
pen_size=5
file_path=""

style = ThemedStyle(root)
style.set_theme("clam")

style.configure("TButton", background="#5a76e2", foreground="white")  # Blue color for buttons
style.configure("TLabel", background="white", foreground="#5a76e2")  # Blue color for labels
style.configure("TFrame", background="#5a76e2")  # Blue color for frames
style.configure("Vertical.TScrollbar", troughcolor="#5a76e2", slidercolor="white")  # Blue color for scrollbars


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



left_frame = tk.Frame(root,width=200,height=600,bg="white")
left_frame.pack(side="left",fill="y")

canvas = tk.Canvas(root,width=750,height=600)
canvas.pack()

image_button = ttk.Button(left_frame, text="Add Image", command=add_image, style="TButton")
image_button.pack(pady=15, padx=10)

color_button = ttk.Button(left_frame, text="Change Pen Color", command=change_color, style="TButton")
color_button.pack(pady=5, padx=10)

pen_size_frame = tk.Frame(left_frame, bg=button1)
pen_size_frame.pack(pady=15, padx=10)
pen_size_1 = tk.Scale(pen_size_frame, from_=1, to=300, orient="horizontal", command=update_pen_size)#, bg="black", fg=button_text)
pen_size_1.pack(side="left")

filter_label = tk.Label(left_frame, text="Select Filter", bg="white")
filter_label.pack(pady=10, padx=10)
filters = ["Orignal", "Black and White", "Blur", "Emboss", "Sharpen", "Smooth", "Mirror", "Auto Contrast", "Contour",
           "Boundary Enhance"]
filter_combox = ttk.Combobox(left_frame, values=filters, textvariable="Original", style="TCombobox", foreground="black")
filter_combox.set("Original")
filter_combox.pack(pady=15, padx=10)

clear_button = ttk.Button(left_frame, text="Clear", command=clear_canvas, style="TButton")
clear_button.pack(pady=15, padx=10)

clear_all = ttk.Button(left_frame, text="Clear All", command=clear_canvas_all, style="TButton")
clear_all.pack(pady=15, padx=10)

filter_combox.bind("<<ComboboxSelected>>",lambda event: apply_filter(filter_combox.get()))

canvas.bind("<B1-Motion>",draw) #B1 motion is when you left click and drag cursor
root.mainloop()