'''
Created on 2017. 9. 13.

@author: 이세희
'''
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.models import load_model
from using_keras import loadData as ld
from click.core import batch


if __name__ == '__main__':
    test_count = 30
    batch_size = 5
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3), 
                     activation='relu',
                     input_shape=(50, 50, 3)))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dense(3, activation='softmax'))
    
    train_generator = ld.getTrain_Generator('../images/buildings/train', batch_size)
    test_generator = ld.getTest_Generator('../images/buildings/test', batch_size)
    
    model.compile(loss='categorical_crossentropy', 
                  optimizer='adam',
                  metrics=['accuracy'])
    model.fit_generator(
        train_generator,
        steps_per_epoch=50,
        epochs=10,
        validation_data=test_generator,
        validation_steps=test_count/batch_size)
    
    model.save('../models/3classes_image.h5')
    