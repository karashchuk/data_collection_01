import requests
import time
import json
from pprint import pprint
main_link = 'https://weather-ydn-yql.media.yahoo.com/forecastrss'

city = 'Moscow'
consumer_key = 'dj0yJmk9RlhjcjlxWTl3UjZ3JmQ9WVdrOWJHOVliRFozTnpnbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PWRj'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
params = {'oauth_consumer_key':consumer_key,
			'oauth_signature_method': 'HMAC-SHA1' ,
			'oauth_version': '1.0',
			'oauth_signature': 'HqZCFrxEDT9fOJtEfcdwKBmsu7k=' ,
			'oauth_nonce': '0mcBODM9Mq6' ,
			'oauth_timestamp' :   1586365458  ,
	          'location': city,
	          'format' : 'json',
	          'u' : 'c'}
response = requests.get(main_link, headers=headers, params=params)
data = json.loads(response.text)

pprint(data)
with open('weather_yahoo.json', 'w') as f:
    json.dump(data, f, sort_keys=True, indent=2)