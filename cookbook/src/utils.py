import cv2
import os
import numpy as np


# Load images from folder into list
def load_images(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        images.append(img)
        if img is None:
            print(filename)
    return images


# Convert png images to jpg
# Takes cuisine and image filename as string parameters
# Writes image to folder
def png_to_jpg(cuisine, file):
    path = "category/" + cuisine + "/" + file + ".png"
    new = "category/" + cuisine + "/" + file + ".jpg"
    img = cv2.imread(path)
    cv2.imwrite(new, img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])


# Return average RGB values of image
def average_rgb(img):
    b = np.average(img[:, :, 0])
    g = np.average(img[:, :, 1])
    r = np.average(img[:, :, 2])
    avg_rgb = [r, g, b]
    return avg_rgb


# Return average hsv values of image
def average_hsv(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h = np.average(img[:, :, 0])
    s = np.average(img[:, :, 1])
    v = np.average(img[:, :, 2])
    avg_hsv = [h, s, v]
    return avg_hsv


# Concatenate images horizontally
def horizontal_concat(images, interpolation=cv2.INTER_CUBIC):
    min_height = min(img.shape[0] for img in images)
    resized = []
    for img in images:
        resized.append(cv2.resize(img, (int(img.shape[1] * min_height / img.shape[0]), min_height),
                                  interpolation=interpolation))
    return cv2.hconcat(resized)


# Concatenate images vertically
def vertical_concat(images, interpolation=cv2.INTER_CUBIC):
    min_width = min(img.shape[1] for img in images)
    resized = []
    for img in images:
        resized.append(cv2.resize(img, (min_width, int(img.shape[0] * min_width / img.shape[1])),
                                  interpolation=interpolation))
    return cv2.vconcat(resized)


# Concatenate images horizontally and vertically
def tile_concat(images, interpolation=cv2.INTER_CUBIC):
    resized = [horizontal_concat(image, interpolation=interpolation) for image in images]
    return vertical_concat(resized, interpolation=interpolation)
