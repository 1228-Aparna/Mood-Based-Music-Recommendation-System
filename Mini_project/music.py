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
def Recommend_Songs(pred_class):
    if (pred_class == 'Disgust'):
        Play = Music_Player[Music_Player['mood'] == 1].reset_index(drop=True)
        # print(Play)
        an = []
        a = gen_ran(len(Play))
        print(a)
        for i in a:
            an.append(Play.iloc[i, 0])
        # Play = Play.sort_values(by="popularity", ascending=False)
        # Play = Play[:5].reset_index(drop=True)
        # display(Play)

    elif (pred_class == 'Happy' or pred_class == 'Sad'):

        Play = Music_Player[Music_Player['mood'] == 0].reset_index(drop=True)
        # print(Play)
        an = []
        a = gen_ran(len(Play))
        print(a)
        for i in a:
            an.append(Play.iloc[i, 0])
        # Play = Play[:5].reset_index(drop=True)
        # display(Play)


    elif (pred_class == 'Fear' or pred_class == 'Anger'):

        Play = Music_Player[Music_Player['mood'] == 3].reset_index(drop=True)
        # print(Play)
        an = []
        a = gen_ran(len(Play))
        print(a)
        for i in a:
            an.append(Play.iloc[i, 0])
        # Play = Play.sort_values(by="popularity", ascending=False)
        # Play = Play[:5].reset_index(drop=True)
        # display(Play)

    elif (pred_class == 'Surprise' or pred_class == 'Neutral'):

        Play = Music_Player[Music_Player['mood'] == 2].reset_index(drop=True)
        # print(Play)
        an = []
        a = gen_ran(len(Play))
        print(a)
        for i in a:
            an.append(Play.iloc[i, 0])
        # Play = Play.sort_values(by="popularity", ascending=False)
        # Play = Play[:5].reset_index(drop=True)
        # display(Play)
    return an, Play
from tensorflow import keras
import numpy as np
import cv2

emotion = ['Anger', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

model = keras.models.load_model("C:/Users/admin/Downloads/model.h5")
font = cv2.FONT_HERSHEY_SIMPLEX
cam = cv2.VideoCapture(0)
face_cas = cv2.CascadeClassifier('C:/Users/admin/Downloads/frontalface.xml')
vid = cv2.VideoCapture(0)
# a = 0
while True:
    ret, frame = cam.read()
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # gray = cv2.flip(gray,1)
        faces = face_cas.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            face_component = gray[y:y + h, x:x + w]
            fc = cv2.resize(face_component, (48, 48))
            inp = np.reshape(fc, (1, 48, 48, 1)).astype(np.float32)
            inp = inp / 255.
            prediction = model.predict(inp)
            em = emotion[np.argmax(prediction)]
            score = np.max(prediction)
            cv2.putText(frame, em + "  " + str(score * 100) + '%', (x, y), font, 1, (0, 255, 0), 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.imshow("image", frame)
        #print(em)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        print('Error')

cam.release()
cv2.destroyAllWindows()

print("You seem to be "+em)
print("Try listening to the playlist personalised according to your mood :)")
song_names, df = Recommend_Songs(em)
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
