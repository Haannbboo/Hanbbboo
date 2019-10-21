#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 21:23:32 2019

@author: hanbo
"""

from keras.models import Sequential
from keras.layers import Dense
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Flatten

from keras.utils import to_categorical

from keras.datasets import mnist


def myCNN(X_train, y_train, test=None, verbose=1):
    model = Sequential()
    
    model.add(Conv2D(96, kernel_size=(5, 5), input_shape=(28, 28, 1), activation='relu'))
    model.add(MaxPooling2D((3, 3), strides=(2, 2)))
    
    model.add(Conv2D(256, kernel_size=(5, 5), padding='same', activation='relu'))  
    model.add(MaxPooling2D((3, 3), strides=(2, 2)))
    
    model.add(Conv2D(384, kernel_size=(3, 3), padding='same', activation='relu'))
    model.add(Conv2D(384, kernel_size=(3, 3), padding='same', activation='relu'))
    model.add(Conv2D(256, kernel_size=(3, 3), padding='same', activation='relu'))
    model.add(MaxPooling2D((3, 3), strides=(2, 2)))
    
    model.add(Flatten())
    model.add(Dense(10, activation='softmax'))
    
    model.compile(loss='logcosh',optimizer='adam',metrics=['accuracy'])  

    r = model.fit(X_train, y_train, epochs=100, batch_size=256, validation_data=test, verbose=verbose)
    
    return r, model


def prepare_data():
    (X_train, y_train), (X_test, y_test) = mnist.load_data()

    X_train = X_train.reshape(-1, 28, 28, 1)
    X_train = X_train.astype('float32')
    
    X_test= X_test.reshape(-1, 28, 28, 1)
    X_test = X_test.astype('float32')
    
    y_train = to_categorical(y_train,10)
    y_test = to_categorical(y_test,10)
    return X_train, y_train, X_test, y_test

X_train, y_train, X_test, y_test = prepare_data()
r, model = myCNN(X_train, y_train, test=(X_test, y_test))