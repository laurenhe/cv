import cv2
import os


# Load images from folder into list
def load_images(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        images.append(img)
    return images


# Convert png images to jpg
def png_to_jpg(cuisine, file):
    path = "category/" + cuisine + "/" + file + ".png"
    new = "category/" + cuisine + "/" + file + ".jpg"
    image = cv2.imread(path)
    cv2.imwrite(new, image, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
