# !/usr/bin/python3
"""
This script takes a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response.
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    # 1. Get arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # 2. Prepare the Data
    # We create a dictionary of our data
    values = {'email': email}

    # We must encode the data into a query string (format: key=value)
    # and then encode that string into bytes (ascii)
    data = urllib.parse.urlencode(values).encode('ascii')

    # 3. Create the Request object
    # By passing the 'data' argument, urllib automatically uses the POST method
    req = urllib.request.Request(url, data)

    # 4. Send the Request and Read Response
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))
