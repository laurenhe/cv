import cv2
import numpy as np
import utils
import splitfolders


def main():
    ita = utils.load_images("category/italian")
    # fre = utils.load_images("category/french")
    # ita_tile = utils.tile_concat([ita[0:15], ita[15:31], ita[31:46], ita[46:61], ita[61:76], ita[76:91], ita[91:106],
    #                               ita[106:121], ita[121:136], ita[136:151], ita[151:166], ita[166:181]])
    # cv2.imwrite("category/italian.jpg", ita_tile)
    splitfolders.ratio("category/input", output="category/output", seed=1337, ratio=(.8, .2), group_prefix=None)


if __name__ == "__main__":
    main()
