#!/usr/bin/python3
"""Module to grab data from reddit"""

import requests


def top_ten(subreddit):
    """Function that querries an api
    to return the first 10 hot posts"""
    user_agent = (
        "Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1"
    )
    headers = {"User-Agent": user_agent}
    url = "https://www.reddit.com/r/{}/top.json?limit=10".format(subreddit)
    reddit_data = requests.get(url, headers=headers, allow_redirects=False)
    if reddit_data.status_code in (302, 404):
        return 0
    json_data = reddit_data.json()
    json_data_children = json_data.get('data').get('children')
    for li in json_data_children:
        print(li.get('data').get('title'))
