import requests
import os 
import urllib
from dotenv import load_dotenv


class QueryAPI:

    def make_request(self, user_query, endpoint='search'):
        # endpoint can support these different values: search, news, images, scholar
        
        # Will be using environment variables to protect my API key.
        # In order for this code to work you have to obtain an API key from this link:
        # https://rapidapi.com/apigeek/api/google-search3/
        load_dotenv() # loading the API key
        API_KEY = os.environ.get('API_KEY')

        headers = {
            'x-rapidapi-key': API_KEY,
            'x-rapidapi-host' :'google-search3.p.rapidapi.com'
        }

        '''
            Query parameters:
                q: input query,
                num: number of results returned,
                cr: specify country,
                rl: results language
        '''
        query = {
            'q': user_query,
            'num': 1,
            }


        url = f'https://google-search3.p.rapidapi.com/api/v1/{ endpoint }/'
        response = requests.get(url + urllib.parse.urlencode(query), headers=headers)

        result = response.json()
        return result['results'][0]['link']