
import os
import sys
from six.moves import urllib
import tarfile
import zipfile

DATA_URL = ['https://s3.eu-central-1.amazonaws.com/avg-kitti/data_semantics.zip']
def maybe_download_and_extract(data_dir, DATA_URL, is_zipflie=False, is_tarfile=False):
    for idx, data_url in enumerate(DATA_URL):
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        filename = data_url.split('/')[-1]
        filepath = os.path.join(data_dir, filename)
        if not os.path.exists(filepath):
            def _progress(count, block_size, total_size):
                sys.stdout.write(
                    '\r>> Downloading %s %.1f%%' % (filename, float(count * block_size) / float(total_size) * 100.0))
                sys.stdout.flush()
            filepath, _ = urllib.request.urlretrieve(data_url, filepath, reporthook=_progress)
            statinfo = os.stat(filepath)
            print('Succesfully downloaded', filename, statinfo.st_size, 'bytes.')

if __name__ == '__main__':
    #"/home/groupprofzli/data/ycwang/"
    maybe_download_and_extract('C:/Users/ycwang/Desktop', DATA_URL, is_tarfile=True)