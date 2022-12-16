import tkinter
from tkinter import *
import os
root = Tk()

canvas = Canvas(root, width=1024, height=786)
root.title("MOOD BASED MUSIC RECOMMENDATION SYSTEM")
canvas.pack()
img = PhotoImage(file="C:\\Users\\admin\\Downloads\\music_title.PNG")
canvas.create_image(512, 384, image = img)

def menu_page():
        os.system('menu.py')

go_img = PhotoImage(file="C:\\Users\\admin\\Downloads\\music_start.PNG")
go_button = Button( width=310, height=90, image=go_img, command = menu_page)
go_button.place(relx=0.35, rely=0.65)
root.mainloop()
