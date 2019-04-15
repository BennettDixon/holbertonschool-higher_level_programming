#!/usr/bin/python3
"""script for posting data to star wars api
"""
if __name__ == "__main__":
    import requests
    from requests.auth import HTTPBasicAuth
    import sys
    url = "https://api.github.com/"
    user_url = url + "user"
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get(user_url,
                            auth=HTTPBasicAuth(username,
                                               password))
    if response.status_code == requests.codes.ok and len(response.text) > 0:
        try:
            my_obj = response.json()
            print(my_obj.get('id'))
        except ValueError as invalid_json:
            print('Not a valid JSON')
    else:
        print(None)
