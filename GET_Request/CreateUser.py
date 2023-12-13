import requests
import json
import os
import jsonpath

url = "https://reqres.in/api/users"

#file = open('/home/myatthinkhine/Documents/Myat/API_Json/CreateUser.json','r')

cur_dir = os.path.dirname(os.path.realpath(__file__))
#construct the path to config.json using a relative path
conf_path = os.path.join(cur_dir, '..', 'CreateUser.json')

files = open(conf_path, "r") 
json_input = files.read()
request_json = json.loads(json_input)
print(request_json)

#Make Post Request

response = requests.post(url, request_json)
print(response.content)
assert response.status_code == 201

#Fetch Header from Response
#print("Header >> ",response.headers)

#Parse Response to Json Format
response_json = json.loads(response.text)

#pick id using json path
id =  jsonpath.jsonpath(response_json,'id')

print("id >> " ,id[0])




