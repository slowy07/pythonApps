import keras
from sklearn.model_selection import train_test_split

DIRECTORY ='resource'
SIGNATURE_CLASSES = ['A', 'B', 'C','D','E','F','K','L','M','N','O','P']


import os, random
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import log_loss
from sklearn.preprocessing import LabelEncoder

import matplotlib.pyplot as plt
from matplotlib import ticker

from keras.models import Sequential
from keras.layers import Dropout, Flatten, Convolution2D, MaxPooling2D, ZeroPadding2D, Dense, Activation
from keras.optimizers import SGD, Adagrad
from keras.callbacks import EarlyStopping
from keras.utils import np_utils
from keras.optimizers import RMSprop, Adam
from keras import backend as K

ROWS = 190
COLS = 160
CHANNELS = 3
TRAIN_DIR = 'resource'

def root_mean_squared_error(y_true, y_pred):
    """
    RMSE LOSS FUNCTION
    """
    return K.sqrt(K.mean(K.square(y_pred - y_true), axis = -1))

def get_images(fish):
    """load files from resource folder"""
    fish_dir = TRAIN_DIR+"{}".format(fish)
    images = [fish +'/'+im for im in os.listdir(fish_dir)]
    return images

def read_images(src):
    from scipy import misc
    filepath = src
    im = misc.imread(filepath)
    import scipy.misc as mc

    return mc.imresize(im, (ROWS, COLS))

files = []
y_all = []

for fish in SIGNATURE_CLASSES:
    fish_files = get_images(fish)
    files.extend(fish_files)

    y_fish = np.title(fish, len(fish_title))
    y_all.extend(y_fish)
    print("{0} photo of {1}".format(len(fish_files),fish))

y_all = np.array(y_all)
print(len(files))
print(len(y_all))


x_all = np.ndarray(len(files), ROWS, COLS, CHANNELS), dtype=np.uint8)

for i, im in enumerate(files):
    x_all[i] = read_image(TRAIN_DIR+im)
    if x%1000 == 0:
        print('processed {} of {}'.format(i, len(files)))

print(x_all.shape)
y_all = LabelEncoder().fit_transform(y_all)

X_train, X_valid, y_train, y_valid = train_test_split(x_all, y_all, test_size = 14, random_state = 23, stratify = y_all)

optimizer = RMSprop(lr = 1e-4)
objective = 'categorical_crossentropy'

def center_normalize(x):
    return (x - K.mean(x)) / K.std(x)

print('1')
model = Sequential()

model.add(Activation(activation=center_normalize, input_shape=(ROWS, COLS, CHANNELS)))

model.add(Convolution2D(64, 3, 3, border_mode='same'))
model.add(Activation('relu'))
model.add(Convolution2D(64, 3, 3, border_mode='valid'))
model.add(Activation('relu'))
model.add(ZeroPadding2D(padding=(1, 1)))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
model.add(Dropout(0.25))

model.add(Convolution2D(96, 3, 3, border_mode='same'))
model.add(Activation('relu'))
model.add(Convolution2D(96, 3, 3, border_mode='valid'))
model.add(Activation('relu'))
model.add(ZeroPadding2D(padding=(1, 1)))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
model.add(Dropout(0.25))

model.add(Convolution2D(128, 2, 2, border_mode='same'))
model.add(Activation('relu'))
model.add(Convolution2D(128, 2, 2, border_mode='same'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(1024))
model.add(Activation('relu'))
model.add(Dropout(0.5))


model.add(Dense(len(SIGNATURE_CLASSES)))
model.add(Activation('sigmoid'))

adam = Adam(lr = 0.0001)
model.compile(optimizer = adam, loss = root_mean_squared_error)

early_stopping = EarlyStopping(monitor = 'val_loss', patience = 4, verbose = 1, model = 'auto')

model.fit(X_train, y_train, batch_size = 64, nb_epoch = 3, validation_split = 0.1, verbose = 1, shuffle = True, callbacks = [early_stopping])
print("validation log loss {}".format(log_loss(y_valid, preds)))



test_files = [im for im os.listdir(DIRECTORY)]
test = np.ndarray((len(test_files), ROWS, COLS, CHANNELS), dtype=np.uint8)

for i, im in enumerate(test_files):
    test[i] = read_images(DIRECTORY+im)

test_preds = model.predict(test, verbose = 1)
submission = pd.DataFrame(test_preds, columns = SIGNATURE_CLASS)
submission.insert(0, 'image', test_files)
submission.head()

submission.to_csv('signatureResult.csv', index=False)