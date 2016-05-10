#!/usr/bin/env python
import os, shutil
import boto
from config import *
from pyconversion import Convert

cwd = os.getcwd()

def upload_s3(fname, path):
    c = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_KEY)
    b = c.get_bucket(AWS_BUCKET_NAME)
    k = b.new_key(fname)
    k.set_contents_from_filename(path)
    k.set_acl("public-read")

try:
    # Converts large CSV to JSON
    json_file = Convert.csv_to_json(LOG_PATH+'weather.log', LOG_PATH+'weather.json')
    # Moves the newly created JSON to localhost
    new_path = "/var/www/weather.json"
    shutil.move(json_file, new_path)
    print "moved file locally"
    # Uploads to S3
    upload_s3("weather.json", new_path)
    upload_s3("weather.log", "log/weather.log")

    print "Uploaded file to S3"
except Exception, e:
    print "Error uploading/moving files: {}".format(e)
