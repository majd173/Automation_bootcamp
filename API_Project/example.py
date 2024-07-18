import requests

url = "https://faceanalyzer-ai.p.rapidapi.com/"

headers = {
	"x-rapidapi-key": "fd1c8eb3eamshe5b076ef4fa1397p1b3ab5jsn4357cdabb360",
	"x-rapidapi-host": "faceanalyzer-ai.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())