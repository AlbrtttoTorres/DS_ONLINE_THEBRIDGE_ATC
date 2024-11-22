print("Your TMDB API key is {{a5348ff849c18eeb4c2d31dfbf30eb30}}")
import json
import requests
from pprint import pprint

api_key = '{{a5348ff849c18eeb4c2d31dfbf30eb30}}'
language = 'en-US'

response = requests.get("https://api.themoviedb.org/3/movie/popular", 
                        params={'api_key':api_key,
                                'language':language})

#beautifying and printing the JSON response
pprint(response.json())
