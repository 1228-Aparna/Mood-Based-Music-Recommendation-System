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
while (True):
    # a = a + 1
    ret, frame = vid.read()
    cv2.imshow("Capturing the image for cartoonifying", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    cv2.imwrite("snap.jpg", frame)
vid.release()
cv2.destroyAllWindows()
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

        if cv2.waitKey(1) == ord('q'):
            break
    else:
        print('Error')

cam.release()
cv2.destroyAllWindows()
x = True
while x:
    # Reading the Image
    image = cv2.imread("snap.jpg")
    # Finding the Edges of Image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 7)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 10)
    # Making a Cartoon of the image
    # first transformation
    color = cv2.bilateralFilter(image, 12, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    # second transformation
    # In the second transformation, we will try to blur the image with an edge-preserving filter and
    # adding a threshold to the edges. For this, we will use Gaussian Blur.
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # apply gaussian blur
    grayImage = cv2.GaussianBlur(grayImage, (3, 3), 0)
    # detect edges
    edgeImage = cv2.Laplacian(grayImage
                              , -1, ksize=5)
    edgeImage = 255 - edgeImage
    # threshold image
    ret, edgeImage = cv2.threshold(edgeImage, 150, 255, cv2.THRESH_BINARY)
    # blur images heavily using edgePreservingFilter
    edgePreservingImage = cv2.edgePreservingFilter(image, flags=2, sigma_s=50, sigma_r=0.4)
    # create output matrix
    output = np.zeros(grayImage.shape)
    # combine cartoon image and edges image
    output = cv2.bitwise_and(edgePreservingImage, edgePreservingImage, mask=edgeImage)
    # cartoon image
    cv2.imshow("Cartoon", output)
    cv2.waitKey(0)  # Used to close the image window using '0'
    cv2.destroyAllWindows()
    x = False