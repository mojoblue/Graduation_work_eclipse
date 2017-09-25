'''
Created on 2017. 9. 13.

@author: 이세희
'''

from keras.models import load_model
from using_keras import loadData as ld
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
#     model = load_model
    tag = {0:'63빌딩', 1: '경회루', 2: '광화문'}
#     train_generator = ld.getTrain_Generator('../images/buildings/train', 2)
    test_generator = ld.getTest_Generator('../images/buildings/test', 5)
    #Image generator의 batch_size를 가져옴
    batch_size = test_generator.batch_size
    #Image generator에 있는 모든 image 파일의 수 : n
    n = test_generator.n
    
    for i in range(0, int(n/batch_size)):
        x, y = test_generator.next()
        for x_hat, y_hat in zip(x, y):
#             print(x_hat)
            print(tag[np.argmax(y_hat)])
            plt.imshow(x_hat)
            plt.show()
#     print(test_generator.total_batches_seen)
#     print(test_generator.batch_index)
#     print(test_generator.batch_size)
#     print(test_generator.target_size)
#     print(test_generator.n)
#     test_generator.
#     for x, y in test_generator:
#         print(x, y)
#         count+=1
#         print(count)
#     for i in range(0, 2):
#         print(x[i])
#         print(y[i])
#         plt.imshow(x[i])
#         plt.show()