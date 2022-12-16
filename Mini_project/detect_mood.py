import tkinter
from music import songs, song_names
from _cv_file import emtn
from tkinter import *
import os
import webbrowser
root = Tk()
canvas = Canvas(root, width=1024, height=786)
root.title("DETECT MOOD")
canvas.pack()
#songs = music.songs
#song_names = music.song_names
#em = _cv_file.em
def callback(url):
    webbrowser.open_new_tab(url)
print(len(songs))
print(len(song_names))
x, y = 200, 200

for i in range(len(songs)):
    song = song_names[i]
    link1 = Label(root, text="Hey, you seem to be "+ emtn, font=('Helveticabold', 15), fg="black")
    link1.place(x = 50, y = 50)
    link2 = Label(root, text="Try listening to the playlist personalised according to your mood :)", font=('Helveticabold', 15), fg="black")
    link2.place(x = 80, y = 80)
    link = Label(root, text=song, font=('Helveticabold', 15), fg="blue", cursor="hand2")
    link.place(x=x, y=y)
    y+=50
    link.bind("<Button-1>", lambda e:
    callback(songs[i]))
    #canvas.create_text(x, y, text=i, fill="black", font=('Helvetica 15 bold'))
    #webbrowser.open(i)

root.mainloop()

