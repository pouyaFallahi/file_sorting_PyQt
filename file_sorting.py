import os
import shutil


def len_files(directory_to_sort):
    return len(os.listdir(directory_to_sort))


def file_sorting(directory_to_sort):
    for filename in os.listdir(directory_to_sort):
        try:
            if ((filename.endswith('.pdf') or filename.endswith('.doc') or
                 filename.endswith('.docx') or filename.endswith('.txt') or
                 filename.endswith('.rtf') or filename.endswith('.ppt') or
                 filename.endswith('.pptx') or filename.endswith('.odt') or
                 filename.endswith('.ods') or filename.endswith('.odp')) or
                    filename.endswith('.xls') or filename.endswith('.xlsx') or
                    filename.endswith('.csv') or filename.endswith('.xml') or
                    filename.endswith('.ott') or filename.endswith('.fodt') or
                    filename.endswith('.uot') or filename.endswith('.dotx') or
                    filename.endswith('.ots') or filename.endswith('.fods') or
                    filename.endswith('.uos') or filename.endswith('.xltx') or
                    filename.endswith('.xlt') or filename.endswith('.dif') or
                    filename.endswith('.dbf')):
                if not os.path.exists(directory_to_sort + 'Documents'):
                    os.mkdir(directory_to_sort + 'Documents')
                shutil.move(os.path.join(directory_to_sort, filename), directory_to_sort + 'Documents')


            elif (filename.endswith('.jpg') or filename.endswith('.jpeg') or
                  filename.endswith('.png') or filename.endswith('.gif') or
                  filename.endswith('.bmp') or filename.endswith('.tif') or
                  filename.endswith('.tiff') or filename.endswith('.heic') or
                  filename.endswith('.JPG')):
                if not os.path.exists(directory_to_sort + 'Pictures'):
                    os.mkdir(directory_to_sort + 'Pictures')
                shutil.move(os.path.join(directory_to_sort, filename), directory_to_sort + 'Pictures')


            elif (filename.endswith('.mp3') or filename.endswith('.wav') or
                  filename.endswith('.mp4') or filename.endswith('.avi') or
                  filename.endswith('.mkv') or filename.endswith('.mpg') or
                  filename.endswith('.mpeg') or filename.endswith('.flv') or
                  filename.endswith('.mov') or filename.endswith('.wmv') or
                  filename.endswith('.m4v') or filename.endswith('.webm') or
                  filename.endswith('.3gp')):
                if not os.path.exists(directory_to_sort + 'Videos'):
                    os.mkdir(directory_to_sort + 'Videos')
                shutil.move(os.path.join(directory_to_sort, filename), directory_to_sort + 'Videos')

            elif (filename.endswith('.rar') or filename.endswith('.zip') or
                  filename.endswith('.7z') or filename.endswith('.iso') or
                  filename.endswith('.tar') or filename.endswith('.gz') or
                  filename.endswith('.tar.gz') or filename.endswith('.tar.bz2') or
                  filename.endswith('.tar.xz') or filename.endswith('.tar.lzma') or
                  filename.endswith('.tar.zst') or filename.endswith('.tar.lz4')):
                if not os.path.exists(directory_to_sort + 'Compressed'):
                    os.mkdir(directory_to_sort + 'Compressed')
                shutil.move(os.path.join(directory_to_sort, filename), directory_to_sort + 'Compressed')

            elif filename.endswith('.exe') or filename.endswith('.deb'):
                if not os.path.exists(directory_to_sort + 'Software'):
                    os.mkdir(directory_to_sort + 'Software')
                shutil.move(os.path.join(directory_to_sort, filename), directory_to_sort + 'Software')

            else:
                continue

        except FileExistsError:
            print(filename, 'already exists in', directory_to_sort)
