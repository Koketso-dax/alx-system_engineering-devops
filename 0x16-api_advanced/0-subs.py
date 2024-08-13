#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests
import requests.exceptions


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-Agent':'0x16-api_advanced:project/u/koketso-dax)'}

    # Make the GET request with no redirects allowed
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    try:
        r = requests.get(url, headers=user_agent,
                         allow_redirects=False)

        if r.status_code == 200:
            subs = r.json().get("data", {}).get("subscribers", 0)
            return subs
        else:
            # Handle cases for status code errors
            return 0
    except requests.exceptions.RequestException:
        return 0
