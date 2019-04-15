#!/usr/bin/python3
"""script for posting data to star wars api
"""
if __name__ == "__main__":
    import requests
    import sys
    url = "https://swapi.co/api/people/"
    search_url = url + "?search="
    if len(sys.argv) > 1:
        search_url += sys.argv[1]
    else:
        search_url = url
    response = requests.get(search_url)
    if response.status_code != requests.codes.ok or len(response.text) <= 0:
        print('No result')
        sys.exit()
    else:
        try:
            my_obj = response.json()
            if len(my_obj) == 0:
                print('No result')
                sys.exit()
            print('Number of results: {}'.format(my_obj.get('count')))
            results = my_obj.get('results')
            for result in results:
                print(result.get('name'))
        except ValueError as invalid_json:
            print('Not a valid JSON')
