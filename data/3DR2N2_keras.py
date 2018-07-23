from keras.models import Sequential
from keras.layers.core import Flatten, Dense, Dropout
from keras.layers.convolutional import Convolution2D, MaxPooling2D, ZeroPadding2D
from keras.optimizers import SGD
import cv2, numpy as np

def r2n2():

	n_convfilter = [96, 128, 256, 256, 256, 256]
    n_fc_filters = [1024]

	model = Sequential()
	model.add(Convolution2D(n_convfilter[0], 7, 7, activation='relu', input_shape=(3,127,127)))
	model.add(MaxPooling2D((2,2), strides=(2,2)))
	model.add(Convolution2D(n_convfilter[1], 3, 3, activation='relu'))
	model.add(MaxPooling2D((2,2), strides=(2,2)))
	model.add(Convolution2D(n_convfilter[2], 3, 3, activation='relu'))
	model.add(MaxPooling2D((2,2), strides=(2,2)))
	model.add(Convolution2D(n_convfilter[3], 3, 3, activation='relu'))
	model.add(MaxPooling2D((2,2), strides=(2,2)))
	model.add(Convolution2D(n_convfilter[4], 3, 3, activation='relu'))
	model.add(MaxPooling2D((2,2), strides=(2,2)))
	model.add(Convolution2D(n_convfilter[5], 3, 3, activation='relu'))
	model.add(MaxPooling2D((2,2), strides=(2,2)))
	model.add(Flatten())
    model.add(Dense(n_fc_filters[0], activation='relu'))
