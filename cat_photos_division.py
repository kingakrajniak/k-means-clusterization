import cv2
import glob
import numpy as np
from sklearn.cluster import KMeans


def photos_upload(path):  # image upload
    images = [cv2.imread(image) for image in glob.glob(f'{path}*.jpg')]
    return images


def photo_histogram(image):  # converting photos to histograms
    hist = cv2.calcHist([image], [1], None, [8], [0, 256])
    hist = hist / image.size
    return hist


def input_data(images):  # extracting a dataset of histograms
    histograms = np.ndarray([len(images), 8])
    for i in range(0, len(images)):
        histogram = photo_histogram(images[i])
        histograms[i, :] = histogram[:, 0]
    return histograms


images = photos_upload('cat_photos/')
images_train = images[0:40]
images_test = images[40:45]

k_means = KMeans(n_clusters=2)  # dividing data into two clusters
k_means.fit(input_data(images_train))
labels = k_means.labels_

print('------------TRAINING SET------------')  # displaying training data
print(labels)
for i in range(0, len(images_train)):
    images[i] = cv2.resize(images[i], dsize=None, fx=.5, fy=.5)
    if labels[i] == 0:
        cv2.imshow('red_cat', images[i])
        cv2.waitKey(1000)
    elif labels[i] == 1:
        cv2.imshow('black_cat', images[i])
        cv2.waitKey(1000)

predictions = k_means.predict(input_data(images_test))

print('------------TESTING SET------------')  # displaying test data
print(predictions)
for i in range(0, len(images_test)):
    images_test[i] = cv2.resize(images_test[i], dsize=None, fx=.5, fy=.5)
    if predictions[i] == 0:
        cv2.imshow('red_cat_test', images_test[i])
        cv2.waitKey(1000)
    elif predictions[i] == 1:
        cv2.imshow('black_cat_test', images_test[i])
        cv2.waitKey(1000)
