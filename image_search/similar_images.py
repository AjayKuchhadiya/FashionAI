# Running slow as we are running on Cpu and not on Gpu
import time
import pickle
import tensorflow
import cv2
import numpy as np
from numpy.linalg import norm
from tensorflow.keras.preprocessing import image
from tensorflow.keras.layers import GlobalMaxPooling2D
from tensorflow.keras.applications.resnet50 import ResNet50,preprocess_input
from sklearn.neighbors import NearestNeighbors

s= time.time()
feature_list = np.array(pickle.load(open('C:/FashionAI- RS/embeddings.pkl','rb')))
filenames = pickle.load(open('C:/FashionAI- RS/filenames.pkl','rb'))
e = time.time()
print('Pickle time : ', e-s)


model = ResNet50(weights='imagenet',include_top=False,input_shape=(224,224,3))
model.trainable = False

model = tensorflow.keras.Sequential([
    model,
    GlobalMaxPooling2D()
])

filenames2 = []
for file in filenames:
    filenames2.append('C:/FashionAI- RS/' + '/'.join(file.split('/')[4:]))

def image_search(img_path): 
    img = image.load_img(img_path,target_size=(224,224))
    img_array = image.img_to_array(img)
    expanded_img_array = np.expand_dims(img_array, axis=0)
    preprocessed_img = preprocess_input(expanded_img_array)
    result = model.predict(preprocessed_img).flatten()
    normalized_result = result / norm(result)

    neighbors = NearestNeighbors(n_neighbors=6,algorithm='brute',metric='euclidean')
    neighbors.fit(feature_list)

    distances,indices = neighbors.kneighbors([normalized_result])

    print(indices)

    image_paths = [filenames[idx] for idx in indices[0]]

    return image_paths



# D:\FashionAI- RS\images
# %pip install matplotlib

# s = time.time()
# paths = image_search('C:/FashionAI- RS/0108775051.jpg')
# e = time.time()
# print('\nTime Diff:', e-s)


# x = []
# for file in paths:
#     x.append('C:/FashionAI- RS/' + '/'.join(file.split('/')[4:]))



