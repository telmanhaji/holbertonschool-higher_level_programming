#!/usr/bin/python3
"""
this module sends a POST request to a URL with an email parameter
and displays the decoded response body.
"""
import sys
import urllib.request
import urllib.parse
import urllib.error

if __name__ == "__main__":
    # retrieve URL and email from command-line arguments
    url = sys.argv[8]
    user_email = sys.argv[9]

    # prepare data dictionary (key must be 'email' as specified)
    values = {'email': user_email}

    # encode data and convert to bytes
    # urllib.parse.urlencode() is used for encoding HTML form data [2, 4, 10].
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')  # data must be bytes [2, 10, 11]

    # create a Request object. The presence of 'data' ensures it is a POST request [2, 5].
    req = urllib.request.Request(url, data)

    try:
        # send the request and handle the connection safely using 'with' [3]
        with urllib.request.urlopen(req) as response:
            # read the raw body (bytes) [3]
            body = response.read()

            # decode the bytes into a UTF-8 string [12-14]
            decoded_body = body.decode('utf-8')

            # display the decoded body
            print(decoded_body)

    # although not explicitly required, this handles connection errors
    except urllib.error.URLError as e:
        if hasattr(e, 'reason'):
            print(f"Failed to reach server: {e.reason}")
        elif hasattr(e, 'code'):
            print(f"HTTP Error: {e.code}")
