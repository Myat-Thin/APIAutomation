import requests
import json
import jsonpath

#API URL
url = "https://reqres.in/api/users?page=2"

response = requests.get(url)
#print(response)

#Display  Response Content
#print("Header >>>>>",response.headers)
#print("Content >>>",response.content)

#Parse response to Json Format

json_response = json.loads(response.text)
#print("Json Response >>>> ",json_response)

#Fetch value using json path

# pages = jsonpath.jsonpath(json_response,'total_pages')
# assert pages[0] == 2
# print(pages[0])

#Fetch Nested Json

for i in range(0,6):
    first_name = jsonpath.jsonpath(json_response,'data['+str(i)+'].first_name')
    #'data['+str(i)+'].first_name'
    #'data[3]'
    #'data[firstname]'
    print((first_name[0]))



