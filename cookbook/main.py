import cv2
import numpy as np
import utils

def main():
    images = utils.load_images("category/italian")
    print(len(images))


if __name__ == "__main__":
    main()
