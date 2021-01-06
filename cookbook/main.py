import cv2
import numpy as np
import utils


def main():
    ita = utils.load_images("category/italian")
    # fre = utils.load_images("category/french")
    # print(utils.average_rgb(ita[0]))
    # print(utils.average_hsv(ita[0]))
    for img in ita:
       print(img.shape)
    # print(min(img.shape[0] for img in ita))


if __name__ == "__main__":
    main()
