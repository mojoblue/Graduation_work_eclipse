'''
Created on 2017. 9. 12.

@author: 이세희
'''
import os
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import random

tf.app.flags.DEFINE_integer('raw_width', 50, '')
tf.app.flags.DEFINE_integer('raw_height', 50, '')

FLAGS = tf.app.flags.FLAGS
FLAGS.width = 50
FLAGS.height = 50
FLAGS.depth = 3
FLAGS.data_dir = '../images'
FLAGS.batch_size = 32
FLAGS.num_class = 3
batch_index = 0
filenames = []






def get_filename_set(data_set):
    labels = []
    filename_set = []
    
    with open(FLAGS.data_dir + '/labels.txt', encoding='UTF-8') as f:
        for line in f:
            inner_list = [elt.strip() for elt in line.split(',')]
            labels += inner_list
            
    # 각image 해당하는 태그를 할당
    for i, label in enumerate(labels):
        fnameList = os.listdir(FLAGS.data_dir + '/'+ data_set +'/' + label)
        for filename in fnameList:
            filename_set.append([i, FLAGS.data_dir + '/' + data_set + '/' + label + '/' + filename ])
    
    random.shuffle(filename_set)
     # output : [[label번호, 경로], [...], ...]
    label_set = [x[0] for x in filename_set]
    filename_set = [x[1] for x in filename_set]
    return filename_set, label_set



def conversion(filenames):
    filename_queue = tf.train.string_input_producer(filenames)
    reader = tf.WholeFileReader()
    filename, content = reader.read(filename_queue)
#     print(sess.run(filename))
    
filenames, labels= get_filename_set('test')
# print(filenames)    #x_data_paths
# print(labels)   #labels
# sess = tf.Session()
conversion(filenames)

'''
def read_image(filename):
    fne = filename.split('.')[3]
    print(fne)
    value = tf.read_file(filename)
    print(value)
    if fne == 'jpg' or fne == 'JPG':
        decoded_image = tf.image.decode_jpeg(value, channels=FLAGS.depth)
    elif fne == 'png' or fne == 'PNG':
        decoded_image = tf.image.decode_png(value, channels=FLAGS.depth)
    elif fne == 'gif' or fne == 'GIF':
        decoded_image = tf.image.decode_gif(value, channels=FLAGS.depth)
    else:
        decoded_image = None
        
    if decoded_image == None:
        return None
    
    decoded_image =tf.image.decode_jpeg(value, channels=FLAGS.depth)
    resized_image = tf.image.resize_images(decoded_image, (FLAGS.raw_height, FLAGS.raw_width))
    resized_image = tf.cast(resized_image, tf.float32)
    return resized_image
#     print(resized_image)
#     plt.imshow(resized_image)
#     plt.show()
# imgData_set = get_filename_set('test')
# for file in imgData_set:
#     print(read_image(file[1]))
    
    
def convert_images(sess, data_set):
    filename_set = get_filename_set(data_set)
#     for i in range(0, len(filename_set)):
#         print(filename_set[i][1])
    with open('../data/' + data_set + '_data.bin', 'wb') as f:
        for i in range(0, len(filename_set)):
            resized_image = read_image(filename_set[i][1])
            print(resized_image)
#             try:
#                 image = sess.run(resized_image)
#             except Exception as e:
#                 print(e.message)
#                 continue
            if resized_image == None:
                continue
#             print(i, filename_set[i][0], image.shape)
            f.write(chr(filename_set[i][0]).encode())
            break
#             f.write(image.data.encode())
'''
# sess=tf.Session()
# convert_images(sess, 'test')
