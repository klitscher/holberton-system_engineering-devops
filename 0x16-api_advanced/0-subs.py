#!/usr/bin/python3
"""Module to grab data from reddit"""

import requests


def number_of_subscribers(subreddit):
    """Function that querries an api to return the number of subs"""
    user_agent = (
        "Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1"
    )
    headers = {"User-Agent": user_agent}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    reddit_data = requests.get(url, headers=headers, allow_redirects=False)
    if reddit_data.status_code == 404:
        return 0
    json_data = reddit_data.json()
    return(json_data.get('data').get('subscribers'))
