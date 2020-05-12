import os
os_name = 'windows'
pngquant_path = 'bin\windows\pngquant.exe'
tmp_ext = '-fs8.png'

def get_img_without_ext(img_path):
    last_dot_idx = img_path.rfind('.')
    return img_path[:last_dot_idx]

def compress_image(src, dst):
    src_without_ext = get_img_without_ext(src)
    cmd = pngquant_path + ' ' + src + ' --force --ext ' + tmp_ext
    print('processing ' + src + ' ...')
    os.system(cmd)
    os.replace(src_without_ext + tmp_ext, dst)
    print('done!')

def get_all_png_paths(base_dir):
    paths = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if(file.endswith(".png")):
                paths.append(os.path.join(root,file))
    return paths