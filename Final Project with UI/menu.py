
import tkinter
from tkinter import *
import os
root = Tk()

canvas = Canvas(root, width=1024, height=786)
root.title("DETECT AND PLAY")
canvas.pack()
img = PhotoImage(file="C:\\Users\\admin\\Downloads\\music_home.PNG")
canvas.create_image(512, 384, image = img)

def on_choose():
    top = Toplevel()
    top.title("Choose an emotion to play appropriate songs")
    canvas1 = Canvas(top, width = 1024, height = 786)
    canvas1.pack()




    my_img = PhotoImage(file="C:\\Users\\admin\\Downloads\\choose_page.png")
    canvas1.create_image(512, 384, image=my_img)

    happy_img = PhotoImage(file="C:\\Users\\admin\\Downloads\\happy.PNG")
    happy_button = Button(top, width=150, height=150, image=happy_img)
    happy_button.place(relx=0.05, rely=0.17)

    sad_img = PhotoImage(file="C:\\Users\\admin\\Downloads\\sad.PNG")
    sad_button = Button(top, width=150, height=150, image=sad_img)
    sad_button.place(relx=0.30, rely=0.17)

    ang_img = PhotoImage(file="C:\\Users\\admin\\Downloads\\ang.PNG")
    ang_button = Button(top, width=150, height=150, image=ang_img)
    ang_button.place(relx=0.55, rely=0.17)

    neu_img = PhotoImage(file="C:\\Users\\admin\\Downloads\\neu.PNG")
    neu_button = Button(top, width=150, height=150, image=neu_img)
    neu_button.place(relx=0.80, rely=0.17)

    fear_img = PhotoImage(file="C:\\Users\\admin\\Downloads\\fear.PNG")
    fear_button = Button(top, width=150, height=150, image=fear_img)
    fear_button.place(relx=0.15, rely=0.50)

    dis_img = PhotoImage(file="C:\\Users\\admin\\Downloads\\dis.PNG")
    dis_button = Button(top, width=150, height=150, image=dis_img)
    dis_button.place(relx=0.43, rely=0.50)

    sup_img = PhotoImage(file="C:\\Users\\admin\\Downloads\\sup.PNG")
    sup_button = Button(top, width=150, height=150, image=sup_img)
    sup_button.place(relx=0.70, rely=0.50)


    back_img = PhotoImage(file="C:\\Users\\admin\\Downloads\\quit.PNG")
    back_button = Button(top, width=200, height=83, image=back_img, command = top.destroy)
    back_button.place(relx=0.40, rely=0.85)
    my_img.place(relx= 0.5, rely = 0.5)

def on_detect():
    os.system('_cv_file.py')

start_img = PhotoImage(file="C:\\Users\\admin\\Downloads\\choose.PNG")
start_button = Button(width=315, height=83, image=start_img, command=on_choose)
start_button.place(relx=0.15, rely=0.6)
help_img = PhotoImage(file="C:\\Users\\admin\\Downloads\\detect.PNG")
help_button = Button(width=315, height=83, image=help_img, command = on_detect)
help_button.place(relx=0.55, rely=0.6)
exit_img = PhotoImage(file="C:\\Users\\admin\\Downloads\\quit.PNG")
exit_button = Button(width=200, height=83, image=exit_img, command=root.quit)
exit_button.place(relx=0.40, rely=0.8)
root.mainloop()