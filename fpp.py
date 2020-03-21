# -*- coding: utf-8 -*-
"""
###########################################################
Let's try Face Detection API of Face++
###########################################################
Usage: 
  python fpp.py
  py fpp.py

"""
import requests
import base64
import json
import os, sys
import math
import time
from shutil import move
from os import path
from pathlib import Path, PureWindowsPath


def get_apikey():
    #load API Keys
    with open('.apikey', 'r') as f:
        apikey = json.loads(f.read())
    
    return apikey['api_key'], apikey['api_secret']


target_dir = os.getcwd()
target_dir = os.path.join(target_dir, 'data_src', 'aligned')

if not path.isdir(target_dir):
   print("ERROR: Path " + str(target_dir) + " isn't a valid directory")
   exit()

file_count = len(os.listdir(target_dir))

print("Checking " + str(file_count) + " files")

match_path = os.path.join(target_dir, 'female')
male_path = os.path.join(target_dir, 'male')

if not path.isdir(match_path):
   try:
       os.mkdir(match_path)
   except OSError:
       print("Creation of the directory %s failed" % match_path)
   else:
       print("Successfully created the directory %s " % match_path)

if not path.isdir(male_path):
   try:
       os.mkdir(male_path)
   except OSError:
       print("Creation of the directory %s failed" % male_path)
   else:
       print("Successfully created the directory %s " % male_path)

#Get API key
API_KEY, API_SECRET = get_apikey() 

#URL for Web API    
url = 'https://api-us.faceplusplus.com/facepp/v3/detect'

for thisFile in os.listdir(target_dir):

    file_name = os.path.join(target_dir, thisFile)

    #Open imagefile with binary (base64)
    with open(file_name, 'rb') as f:
        img_in = f.read()

    img_file = base64.encodebytes(img_in)

    #Set configuration
    config = {'api_key':API_KEY,
              'api_secret':API_SECRET,
              'image_base64':img_file,
              'return_attributes':'gender,age'}

    # POST to Web API
    res = requests.post(url, data=config)

    time.sleep(1)

    # Load json data
    data = json.loads(res.text)

    for face in data['faces']:
        # Get attributes from API
        if 'attributes' in face:
            gender = face['attributes']['gender']['value']
            age = face['attributes']['age']['value']

            if gender == 'Female':
                if age < 30 and age > 15:
                    match_file = os.path.join(match_path, thisFile)
                    if os.path.isfile(file_name):
                        move(
                            file_name, match_file)

            elif gender == 'Male':
                male_file = os.path.join(male_path, thisFile)
                if os.path.isfile(file_name):
                    move(
                        file_name, male_file)

