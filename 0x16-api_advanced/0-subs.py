#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        return

    user_agent = {'User-Agent': '0x16-api_advanced:v0.0.1 \
                  (by /u/NearbyProposal7738)'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    r = requests.get(url, headers=user_agent, allow_redirects=False)

    if r.status_code == 200:
        return (r.json()["data"]["subscribers"])
    else:
        return (0) 
