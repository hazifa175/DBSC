import os
import sys

# Flask
from flask import Flask, redirect, url_for, request, render_template, Response, jsonify, redirect
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Some utilites
import numpy as np
from util import base64_to_pil

# Declare a flask app
app = Flask(__name__)

from tensorflow.keras.applications.inception_v3 import InceptionV3
model = InceptionV3(weights='imagenet')

print('Model loaded. Check http://127.0.0.1:5000/')

# Model saved with Keras model.save()
MODEL_PATH = 'models/your_model.h5'


def model_predict(img, model):
    img = img.resize((299,299))

    # Preprocessing the image
    x = image.img_to_array(img)
    # x = np.true_divide(x, 255)
    x = np.expand_dims(x, axis=0)

    x = preprocess_input(x, mode='tf')

    preds = model.predict(x)
    return preds

#------NAVIGATION-----------

@app.route("/index") #HOME
def index():
    return render_template("index.html")

@app.route('/predict', methods=['GET'])
def prediction():
    return render_template('prediction.html')

@app.route('/predict', methods=['GET','POST'])  #RECOGNIZE DOG BREED 
def predict():
    if request.method == 'POST':
        # Get the image from post request
        img = base64_to_pil(request.json)

        # Save the image to ./uploads
        # img.save("./uploads/image.png")

        # Make prediction
        preds = model_predict(img, model)

        # Process your result 
        pred_proba = "{:.3f}".format(np.amax(preds))    # Max probability
        pred_class = decode_predictions(preds, top=1)   

        result = str(pred_class[0][0][1])               # Convert to string
        result = result.replace('_', ' ').capitalize()
        
        # Serialize the result, you can add additional fields
        return jsonify(result=result, probability=pred_proba)

    return None

@app.route("/adopt")
def adopt():
    return render_template("adoption.html")

@app.route("/petcare")  # CARE TIPS
def petcare():
    return render_template("petcare.html")


@app.route("/diagnose") # DIAGNOSE
def diagnose():
    return render_template("diagnose.html")


#----------END NAVIGATION--------------------


# ------------------7 DISEASE------------------
@app.route("/diagnose/fleas")
def fleas():
    return render_template("diagnose/fleas.html")

 
@app.route("/diagnose/tick")
def tick():
    return render_template("diagnose/tick.html")

@app.route("/diagnose/otitis")
def otitis():
    return render_template("diagnose/otitis.html")

    
@app.route("/diagnose/scabies")
def scabies():
    return render_template("diagnose/scabies.html")

@app.route("/diagnose/rage")
def rage():
    return render_template("diagnose/rage.html")

@app.route("/diagnose/distemper")
def distemper():
    return render_template("diagnose/distemper.html")

    
@app.route("/diagnose/osteoarthritis")
def osteoarthritis():
    return render_template("diagnose/osteoarthritis.html")

#-------END DISEASE------------------------------



#--------------DOG ADOPT LIST-------------------

@app.route("/adopt/hound")
def hound():
    return render_template("adopt/hound.html")

@app.route("/adopt/terrier")
def terrier():
    return render_template("adopt/terrier.html")

@app.route("/adopt/toy")
def toy():
    return render_template("adopt/toy.html")

@app.route("/adopt/spaniel")
def spaniel():
    return render_template("adopt/spaniel.html")

@app.route("/adopt/herding")
def herding():
    return render_template("adopt/herding.html")

@app.route("/adopt/working")
def working():
    return render_template("adopt/working.html")

@app.route("/adopt/non-sporting")
def nonsporting():
    return render_template("adopt/non-sporting.html")

@app.route("/adopt/sporting")
def sporting():
    return render_template("adopt/sporting.html")


@app.route("/adopt/utility")
def utility():
    return render_template("adopt/utility.html")

@app.route("/adopt/gundog")
def gundog():
    return render_template("adopt/gundog.html")

#----------------------------------------

if __name__ == '__main__':
    # app.run(port=5002, threaded=False)

    # Serve the app with gevent
    http_server = WSGIServer(('0.0.0.0', 5000), app)
    http_server.serve_forever()
