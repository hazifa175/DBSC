from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

# labels
classNames = []
classFile = 'model\\labels.txt'
with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

# Print image
image = Image.open('static\\images\\Hound\\Afghan_hound_00132.jpg')

# Load the model
model = load_model('model\\model.h5')

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.


#resize the image to a 224x224 with the same strategy as in TM2:
#resizing the image to be at least 224x224 and then cropping from the center

#turn the image into a numpy array
img_g = np.expand_dims(image, axis=0)

def extact_features(data):
    inception_features = get_features(InceptionV3, inception_preprocessor, img_size, data)

    print('Final feature maps shape', inception_features.shape)   
    
    return inception_features

test_features = extact_features(test_data)

# Load

# run the inference
prediction = model.predict(test_features)
# print(prediction)
# print(np.argmax(prediction))
# print(np.max(prediction))
# print(classNames[np.argmax(prediction)])
# #Predict test labels given test data features.

print(f"Predicted label: {classes[np.argmax(predg[0])]}")
print(f"Probability of prediction): {round(np.max(predg[0])) * 100} %")
