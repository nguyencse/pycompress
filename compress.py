import os
import time
import utils
from sys import argv

buyer = argv[1]
my_flutter_packages = argv[2]

# buyer = 'D:\\Sendo\projects\\buyer-mobile-android2'
# my_flutter_packages = 'D:\\Sendo\\projects\\MyFlutter\\.packages'

git_cache = ''

if __name__ == "__main__":

    # detect git cached
    if os.path.exists(my_flutter_packages):
        with open(my_flutter_packages) as fp: 
            for line in fp:
                if '/git/' in line:
                    root_folder = line.find('///')
                    git_folder = line.find('/git/')
                    git_cache = line[root_folder + 3 : git_folder + 5]
                    print('Flutter git cache folder detected: ' + git_cache)
                    break

    # buyer_files = utils.get_all_png_paths(buyer)
    # flutter_files = utils.get_all_png_paths(git_cache)

    buyer_files = utils.get_all_png_paths(buyer)
    flutter_files = utils.get_all_png_paths(git_cache)

    fnames = buyer_files[0] + flutter_files[0]
    fsizes = buyer_files[1] + flutter_files[1]

    print(len(fnames))

    print("*********************************************")
    print("*                                           *")
    print("*              Android team                 *")
    print("*         Resource compressing V1           *")
    print("*                                           *")
    print("*********************************************")

    time_start = time.time()
    
    for idx, fname in enumerate(fnames):
        utils.compress_image(fname, fname)
        utils.progress(count=idx + 1, total=len(fnames), status=fname)

    time_end = time.time()

    print('\rDone in ' + str(round((time_end - time_start) / 1000 / 60, 2)) + 's')

    buyer_files2 = utils.get_all_png_paths(buyer)
    flutter_files2 = utils.get_all_png_paths(git_cache)

    fnames2 = buyer_files2[0] + flutter_files2[0]
    fsizes2 = buyer_files2[1] + flutter_files2[1]

    sum1 = round(sum(fsizes) / 1024, 2)
    sum2 = round(sum(fsizes2) / 1024, 2)

    print('=====BEFORE=====')
    print('Total files: ' + str(len(fnames)))
    print('Total size: ' + str(sum1) + 'KB')
    print('=====AFTER======')
    print('Total files: ' + str(len(fnames2)))
    print('Total size: ' + str(sum2) + 'KB')
    print('=====RESULT=====')
    print('Saved ' + str(round(sum1 - sum2)) + 'KB')