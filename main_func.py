import os
import re
import tinify
import shutil
import webbrowser

from config import web_url
from config import web_name
from config import ACCESS_KEY_ID
from config import ACCESS_KEY_SECRET
from config import OSS_BUCKET_NAME
from config import OSS_ENDPOINT
from config import TINIFY_KEY
from config import TINIFY_PROXY
from config import html_oss_bucket_folder
from config import imgs_oss_bucket_folder
from config import temp_imgs_local_folder
from config import temp_html_local_folder
from config import title

from handle_html import from_url_get_html
from handle_html import delete_useless_code
from handle_html import save_html_file
from handle_html import replace_img_url_prefix

from handle_imgs import get_all_img_url
from handle_imgs import compress_img
from handle_imgs import download_imgs

from upload_files_to_OSS import create_bucket_object
from upload_files_to_OSS import upload_file_to_oss


def create_and_enter_new_folder(folder_name):
    module_path = os.path.dirname(__file__)
    # print(os.getcwd())
    folder_path = module_path+'/'+folder_name
    if os.path.isdir(folder_path):
        pass
    else:
        os.mkdir(folder_path)
    os.chdir(folder_path)


def delete_temp_folder():
    module_path = os.path.dirname(__file__)
    os.chdir(module_path)
    # print(os.getcwd())
    shutil.rmtree(temp_imgs_local_folder)
    shutil.rmtree(temp_html_local_folder)


class PublishWeb:

    def __init__(self):
        self.bucket = create_bucket_object(ACCESS_KEY_ID, ACCESS_KEY_SECRET, OSS_BUCKET_NAME, OSS_ENDPOINT)
        self.web_url = web_url
        self.web_name = web_name
        self.web_file_name = web_name + '.html'
        self.oss_file_prefix_url = 'https://' + OSS_BUCKET_NAME + '.' + OSS_ENDPOINT + '/'
        self.imgs_oss_bucket_folder = imgs_oss_bucket_folder
        self.html_oss_bucket_folder = html_oss_bucket_folder
        self.title = title

    # get html source code and delete redundant code
    def generate_html_file(self):
        html = from_url_get_html(self.web_url)
        html = delete_useless_code(html, title)

        # TinyPNG config
        tinify.key = TINIFY_KEY
        tinify.proxy = TINIFY_PROXY

        # create local img folder
        create_and_enter_new_folder(temp_imgs_local_folder)
        img_url = get_all_img_url(html)

        # compress and upload imgs
        for url in img_url:
            # get img name
            img_name = re.sub(r'.*/', '', url)

            # compress and save img
            # compress_img(url, img_name)

            # download imgs
            download_imgs(url, img_name)

            # upload img to oss
            upload_file_to_oss(img_name, self.imgs_oss_bucket_folder, self.bucket)

            # replace url prefix
            img_oss_prefix_url = self.oss_file_prefix_url + '/' + self.imgs_oss_bucket_folder + '/'
            new_url = replace_img_url_prefix(url, img_oss_prefix_url)
            html = html.replace(url, new_url)

        # save html file
        create_and_enter_new_folder(temp_html_local_folder)
        save_html_file(self.web_file_name, html)
        print('*' * 50)
        print('\nhtml file saved!')
        print('*' * 50)

        # open local html file
        # module_path = os.path.dirname(__file__)
        # temp_html_local_folder_path = 'file://' + module_path + '/' \
        #                               + temp_html_local_folder + '/' + self.web_file_name
        # webbrowser.open(temp_html_local_folder_path, new=2)

    def upload_html_and_delete_local_temp_file(self):
        module_path = os.path.dirname(__file__)
        temp_html_local_folder_path = module_path + '/' + temp_html_local_folder
        os.chdir(temp_html_local_folder_path)
        # print(temp_html_local_folder_path)

        # upload html file
        upload_file_to_oss(self.web_file_name, self.html_oss_bucket_folder, self.bucket)
        print('*'*50)

        # get final url
        if self.html_oss_bucket_folder:
            final_url = self.oss_file_prefix_url + self.html_oss_bucket_folder + \
                        '/' + self.web_file_name
        else:
            final_url = self.oss_file_prefix_url + self.html_oss_bucket_folder + \
                        self.web_file_name
        print('The OSS html url is: %s\n' % final_url)
        print('*' * 50)

        # open preview url
        webbrowser.open(final_url, new=2)

        # delete temp files
        # delete_temp_folder()
        # print('local temp file deleted!')


if __name__ == '__main__':
    # main()
    pw = PublishWeb()
    pw.generate_html_file()
    pw.upload_html_and_delete_local_temp_file()