import requests

url = "https://currency-converter5.p.rapidapi.com/currency/convert"

querystring = {"format":"json","from":"AUD","to":"CAD","amount":"1"}

headers = {
	"X-RapidAPI-Key": "6fd0f844b5msh18298fe713014a6p13b23ejsn6964dcefac17",
	"X-RapidAPI-Host": "currency-converter5.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())