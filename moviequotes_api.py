import requests

def get_quote():
    headers = {
        'X-RapidAPI-Key': '8wNLNQ7mfymshC9zFxUDJKeHvcrEp1X3EAAjsnWkNmEBOzE4uI',
        'Content-Type': 'application/x-www-form-urlencoded'
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
