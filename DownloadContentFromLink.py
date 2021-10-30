# Script created by Chiriac Adrian Stefan (chr.adrian@yahoo.com)
# Brief : script to download content from a given link


import requests
import shutil
import os
from pathlib import Path


# link = 'LinkToDownload'
# path = r'PathToDownloadFile'


def download_content(link, path):
    # Change the path of download to the desired location
    os.chdir(path)
    # Get the filename from the url by selecting the characters after the last '/'
    file_name = link[link.rindex('/')+1:]
    r = requests.get(link, stream = True,
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'})
    type = r.headers.get('content-type')
    print('File type: ' + type)
    # Add adequate extension if missing
    if 'image/jpeg' in type and '.' not in type:
        file_name = file_name + '.jpg'
    if 'image/gif' in type and '.' not in type:
        file_name = file_name + '.gif'
    if 'video/mp4' in type and '.' not in type:
        file_name = file_name + '.mp4'
    if 'UTF-8' not in type:
        # Download the file
        with open(file_name, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
        # Get the size of the file in Bytes
        size = Path(file_name).stat().st_size
        # Get the size of the file in MB
        mb_factor = float(1 << 20)
        size_mb = int(size) / mb_factor
        limited_size_mb = "{:.3f}".format(size_mb)
        print('File size: ' + str(limited_size_mb) + ' MB')
    else:
        print("Unable to download file")


# download_content(link, path)