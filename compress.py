import os
import utils

folders = ['images', 'images\test']

if __name__ == "__main__":

    filelist = utils.get_all_png_paths('D:\\Sendo\projects\\buyer-mobile-android - Copy')

    print(filelist)

    print('==============')
    print('Total files: ' + str(len(filelist)))

    # for f in filelist:
    #     utils.compress_image(f, f)