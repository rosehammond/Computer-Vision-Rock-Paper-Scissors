import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)


#The main thing to understand is that the variable predictions contains the output of the model, 
# and each element in the output corresponds to the probability of the input image representing 
# a particular class.
#So, for example, if the prediction has the following output: [[0.8, 0.1, 0.05, 0.05]], 
# there is an 80% chance that the input image shows rock, a 10% chance that it shows paper, 
# a 5% chance that it shows scissors, and a 5% chance that it shows nothing.

#Notice that the prediction is a numpy array with one row and four columns. 
# So first, you need to access the first row, and then get the index of the highest value in the row. 
# Check this link  to see how to get the index of the highest value in a row.

#Before moving on, you need to make sure you understand how Python works. 
# So make sure you've understood the prerequisite content.

#You have to know at least how to effectively use while loops and if statements. 
# Please, don't move on until you have a solid understanding of these concepts.

while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    # Press q to close the window
    print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
