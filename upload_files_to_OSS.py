import oss2
import os
from config import ACCESS_KEY_ID
from config import ACCESS_KEY_SECRET
from config import OSS_BUCKET_NAME
from config import OSS_ENDPOINT

from config import imgs_oss_bucket_folder


def create_bucket_object(ACCESS_KEY_ID, ACCESS_KEY_SECRET, OSS_BUCKET_NAME, OSS_ENDPOINT):
    access_key_id = os.getenv('OSS_TEST_ACCESS_KEY_ID', ACCESS_KEY_ID)
    access_key_secret = os.getenv('OSS_TEST_ACCESS_KEY_SECRET', ACCESS_KEY_SECRET)
    bucket_name = os.getenv('OSS_TEST_BUCKET', OSS_BUCKET_NAME)
    endpoint = os.getenv('OSS_TEST_ENDPOINT', OSS_ENDPOINT)
    bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)
    return bucket


def upload_file_to_oss(filename, folder_name, bucket):
    print('Uploading ' + filename)
    if folder_name:
        oss_filename = folder_name + '/' + filename
    else:
        oss_filename = filename
    bucket.put_object_from_file(oss_filename, filename)
    print(filename + ' uploaded!')


if __name__ == "__main__":
    filename = 'test_img.png'
    bucket = create_bucket_object(ACCESS_KEY_ID, ACCESS_KEY_SECRET, OSS_BUCKET_NAME, OSS_ENDPOINT)
    upload_file_to_oss(filename, imgs_oss_bucket_folder, bucket)