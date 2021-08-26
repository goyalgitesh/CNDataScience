import requests as rq
import json

weather = rq.get('https://api.openaq.org/v1/cities',params={'country' : 'IN'})
ans = weather.json()
