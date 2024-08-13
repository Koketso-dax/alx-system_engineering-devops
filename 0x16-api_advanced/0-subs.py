#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests
import requests.exceptions


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    user_agent = '0x16-api_advanced:project:v1.0.0 (by /u/koketso-dax)'
    # Make the GET request with no redirects allowed
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    try:
        r = requests.get(url, headers={'User-Agent': user_agent},
                         allow_redirects=False)
        # Check if the request was successful and parse JSON
        if r.status_code == 200:
            subs = r.json().get("data", {}).get("subscribers", 0)
            return subs
        else:
            # Handle cases where the status code indicates an error
            return 0
    except requests.exceptions.RequestException:
        return 0
