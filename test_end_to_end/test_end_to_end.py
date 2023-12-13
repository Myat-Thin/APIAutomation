import requests
import json
import jsonpath
import os


cur_dir = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(cur_dir, '..' , 'CreateUser.json')
files = open(config_path,'r')
json_input = files.read()
request_json = json.loads(json_input)