#!/usr/bin/env python
# coding: utf-8

#!/usr/bin/env python
# coding: utf-8

# predict_small.py

"""
Please remember that it is the TensorFlow realization with image_data_foramt = 'channels_last'. If
the env of Keras is 'channels_first', please change it  according to the TensorFlow convention. 

Please give the commands as follows. 

$ python predict_small.py


Make the the necessary changes to adapt to the environment of TensorFlow 2.3, Keras 2.4.3, CUDA Toolkit 
11.0, cuDNN 8.0.1 and CUDA 450.57. In addition, write the new lines of code to replace the deprecated 
code. 
"""

import tensorflow as tf 
import numpy as np
from keras.preprocessing import image
from keras.applications.imagenet_utils import decode_predictions
from keras.preprocessing import image
from mobilenet_v3_func import MobileNetV3Small

# Set up the GPU to avoid the runtime error: Could not create cuDNN handle...
gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)


def preprocess_input(x):
    
    x = image.img_to_array(x)
    x = np.expand_dims(x, axis=0)
    x = np.divide(x, 255.0)
    x = np.subtract(x, 0.5)
    output = np.multiply(x, 2.0)

    return output


if __name__ == '__main__':


    model = MobileNetV3Small(include_top=True, weights='imagenet')
    # -model = MobileNetV3Small(include_top=False, weights='imagenet')
 
    model.summary()

    img_path = '/home/mike/Documents/keras_mobilenet/v3/elephant.jpg'
    img = image.load_img(img_path)
    output = preprocess_input(img)
    print('Input image shape:', output.shape)

    preds = model.predict(output)
    print(np.argmax(preds))
    print('Predicted:', decode_predictions(preds,1))
