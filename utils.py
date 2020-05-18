import os
import sys

os_name = 'windows'
pngquant_path = 'bin\windows\pngquant.exe'
tmp_ext = '-fs8.png'

def get_img_without_ext(img_path):
    last_dot_idx = img_path.rfind('.')
    return img_path[:last_dot_idx]

def compress_image(src, dst):
    src_without_ext = get_img_without_ext(src)
    cmd = pngquant_path + ' ' + src + ' --force --ext ' + tmp_ext
    os.system(cmd)
    os.replace(src_without_ext + tmp_ext, dst)

def get_all_png_paths(base_dir):
    paths = []
    sizes = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if(file.endswith(".png")):
                path = os.path.join(root,file)
                if 'build' not in path:
                    paths.append(path)
                    sizes.append(os.path.getsize(path))
    return paths, sizes

def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()