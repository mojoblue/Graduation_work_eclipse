'''
Created on 2017. 9. 12.

@author: 이세희
'''

from glob import glob
from PIL import Image as image

def pngToJpg(path, dataset):
    pngList = []
    for file in glob(path+dataset+'\\*\\'+'*.png'):
        pngList.append(file)
    
    for path in pngList:
        sp = path.split('\\')
        newPath = "\\".join(sp[0:-1])+"\\"
        filename = sp[-1].split('.')[0]
        im = image.open(path)
        rgb_im = im.convert('RGB')
        rgb_im.save(newPath+filename+'.jpg')    
        print('png converted to : '+newPath+filename+'.jpg')

def gifToJpg(path, dataset):
    gifList = []
    for file in glob(path+dataset+'\\*\\'+'*.gif'):
        gifList.append(file)
        
    for path in gifList:
        sp = path.split('\\')
        newPath = "\\".join(sp[0:-1])+"\\"
        filename = sp[-1].split('.')[0]
        im = image.open(path)
        rgb_im = im.convert('RGB')
        rgb_im.save(newPath+filename+'.jpg')
        print('gif converted to : '+newPath+filename+'.jpg')
        
if __name__ == '__main__':
    path = '..\\images\\'
    pngToJpg(path, 'test')
    pngToJpg(path, 'train')
    gifToJpg(path, 'test')
    gifToJpg(path, 'train')
