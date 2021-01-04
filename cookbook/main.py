import cv2
import numpy as np
import utils

def main():
    img_ita = utils.load_images("category/italian")
    print(len(img_ita))
    img_fre = utils.load_images("category/french")
    print(len(img_fre))


if __name__ == "__main__":
    main()
