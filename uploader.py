#!/usr/bin/env python
import os, shutil
import boto
from config import *
from pyconversion import Convert

cwd = os.getcwd()

def upload_s3(fname, path):
    c = boto.connect_s3(aws_access_key_id, aws_secret_key)
    b = c.get_bucket(aws_bucket_name)
    k = b.new_key(fname)
    k.set_contents_from_filename(path)
    k.set_acl("public-read")

try:
    # converts large CSV to JSON
    json_file = Convert.csv_to_json(log_path+'weather.log', log_path+'weather.json')
    # moves the newly created JSON to localhost
    new_path = "/var/www/weather.json"
    shutil.move(json_file, new_path)
    print "moved file locally"
    # uploads it to S3
    upload_s3("weather.json", new_path)
    upload_s3("weather.log", "log/weather.log")
#    c = boto.connect_s3(aws_access_key_id, aws_secret_key)
#    b = c.get_bucket(aws_bucket_name)
#    k = b.new_key("weather.json")
#    k.set_contents_from_filename(new_path)
#    k.set_acl("public-read")

    print "Uploaded file to S3"
except Exception, e:
    print "Error uploading/moving files: {}".format(e)
