import os
import re
import tinify


def compress_img(img_url, filename):
    print('Compressing '+filename)

    # deal with the blank space in url
    if '' in img_url:
        img_url = re.sub(r' ', '+', img_url)
    source = tinify.from_url(img_url)
    print('Downloading '+filename)
    source.to_file(filename)
    print(filename+' Downloaded!')


def get_all_img_url(html):
    imgurl = []
    imgurl = re.findall(r'https://anima.*?png', html)
    # print(imgurl)
    return imgurl


if __name__ == "__main__":
    weburl = 'https://launchpad.animaapp.com/preview/5mFH3lT/innerpeaceproductintro'
    imgurl = get_all_img_url(weburl)
    img_folder = 'test_imgs'
    creat_img_folder(img_folder)
    compress_img(imgurl[5])
    # for url in imgurl:
    # compress_img(url)

