import requests
import os
from dotenv import load_dotenv

load_dotenv()

X_RapidAPI_Key = os.getenv('X-RapidAPI-Key')
Content_Type = os.getenv('Content-Type')

def get_quote():
    headers = {
        'X-RapidAPI-Key': X_RapidAPI_Key,
        'Content-Type': Content_Type
    }
    response = requests.post('https://andruxnet-random-famous-quotes.p.rapidapi.com/?count=1&cat=movies', headers=headers)
    data = response.json()[0]
    return {
        'quote': data['quote'],
        'author': data['author'],
        'category': data['category']
    }

if __name__ == '__main__':
    # code inside this block will only run if this file is executed directly
    # it won't run if this file is imported as a module in another Python script
    print('Fetching quote...')
    quote = get_quote()
    print(quote)
