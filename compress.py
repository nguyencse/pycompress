import os
import time
import utils

folder = 'D:\\Sendo\projects\\buyer-mobile-android2'

if __name__ == "__main__":

    filelist = utils.get_all_png_paths(folder)
    fnames = filelist[0]
    fsizes = filelist[1]

    print('===================')
    print('====COMPRESSING====')
    print('===================')

    time_start = time.time()
    
    for idx, fname in enumerate(fnames):
        print(str(idx) + ' --> processing ' + fname)
        utils.compress_image(fname, fname)

    time_end = time.time()

    print('Done in ' + str(time_end - time_start) + 's')

    filelist2 = utils.get_all_png_paths(folder)
    fnames2 = filelist2[0]
    fsizes2 = filelist2[1]

    sum1 = sum(fsizes) / 1024
    sum2 = sum(fsizes2) / 1024

    print('=====BEFORE=====')
    print('Total files: ' + str(len(fnames)))
    print('Total size: ' + str(sum1) + 'KB')
    print('=====AFTER======')
    print('Total files: ' + str(len(fnames2)))
    print('Total size: ' + str(sum2) + 'KB')
    print('=====RESULT=====')
    print('Saved ' + str(sum1 - sum2) + 'KB')