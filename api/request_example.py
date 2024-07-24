import requests

url = "https://chatgpt.com/backend-api/prompt_library/?limit=4&offset=0"
#
# headers = {
# 	"Access-Control-Allow-Credentials:": "true",
# 	"Content-Encoding:": "br"
# }

response = requests.post(url, headers=None)

# print(response.json())
print(response.status_code)