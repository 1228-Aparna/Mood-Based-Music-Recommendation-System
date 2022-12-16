import random
import pandas as pd
import numpy as np
from tensorflow import keras
import numpy as np
import cv2
Music_Player = pd.read_csv("C:/Users/admin/Downloads/data_moods.csv")
Music_Player = Music_Player[['name', 'artist', 'mood']]


def gen_ran(ul):
    ls = []
    for i in range(5):
        x = random.randint(1, ul)
        ls.append(x)
    return ls


# gen_ran(15)
def Recommend_Songs():
    Play = Music_Player[Music_Player['mood'] == 0].reset_index(drop=True)
    an = []
    a = gen_ran(len(Play))
    print(a)
    for i in a:
        an.append(Play.iloc[i, 0])
    return an, Play
print("You seem to be Happy")
print("Try listening to the playlist personalised according to your mood :)")
song_names, df = Recommend_Songs()
#print(names)
print(df['artist'].reset_index(drop = True))

songs = []
artists = list(df['artist'])
for i in range(len(song_names)):
    n = str(song_names[i]).replace(" ", "+")
    #print(n)
    a = str(artists[i]).replace(" ", "+")
    url = 'https://www.youtube.com/results?search_query='+n + "+by+" + a
    songs.append(url)
    print(url)