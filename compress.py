import os
import utils

folders = ['images', 'images\test']

if __name__ == "__main__":

    filelist = utils.get_all_png_paths('images')

    print(filelist)

    # for f in filelist:
    #     utils.compress_image(f, f)